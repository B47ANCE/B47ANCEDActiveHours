"""Offline Lua mocks only. Requires development dependency lupa, never game execution."""
from pathlib import Path
import unittest
from lupa import LuaRuntime

ROOT = Path(__file__).resolve().parents[1]
LUA = ROOT / 'proof/B47ANCEDActiveHoursSpeedProof/42/media/lua'
MOCK = r'''
Events={}
for _,name in ipairs({'OnTick','OnZombieUpdate','OnClientCommand','OnServerCommand','OnKeyPressed'}) do
 local handlers={}
 Events[name]={Add=function(fn) handlers[#handlers+1]=fn end, handlers=handlers}
end
function emit(name,...) for _,fn in ipairs(Events[name].handlers) do fn(...) end end
function require(_) end
function isServer() return mode=='S' end
function isClient() return mode~='S' end
SandboxVars={ZombieLore={ActiveOnly=1}}
Keyboard={KEY_LCONTROL=1,KEY_LSHIFT=2,KEY_F6=6,KEY_F7=7,KEY_F8=8,KEY_F9=9,KEY_F10=10,KEY_F11=11}
function isKeyDown(_) return modifiers or false end
players={}
for _,name in ipairs({'A','B'}) do
 local p={name=name}
 function p:isLocalPlayer() return mode==self.name end
 function p:getAccessLevel() return self.name=='A' and 'admin' or 'none' end
 players[name]=p
end
function getSpecificPlayer(_) return players[mode] end
function newZombie()
 local z={id=7,walk='slow1',category=3,scalar=0.60,owner='A',writes=0,x=0,y=0}
 function z:getOnlineID() return self.id end
 function z:isDead() return self.dead or false end
 function z:isCrawling() return self.crawling or false end
 function z:getOwnerPlayer() return players[self.owner] end
 function z:isRemoteZombie() return mode=='S' or self.owner~=mode end
 function z:getWalkType() return self.walk end
 function z:getSpeedType() return self.category end
 function z:getSpeedMod() return self.scalar end
 function z:isRunning() return self.category==1 end
 function z:getActionStateName() return 'WalkToward' end
 function z:getAnimationStateName() return 'walk' end
 function z:getX() return self.x end
 function z:getY() return self.y end
 function z:setWalkType(v) self.walk=v; self.writes=self.writes+1 end
 function z:setSpeedTypeFromWalkType()
  if self.failOnce then self.failOnce=false; error('mock setter failure') end
  self.category=B47AHProof.category(self.walk)
 end
 function z:setSpeedMod(v) self.scalar=v end
 return z
end
Z=newZombie()
'''


def plain(value):
    if hasattr(value, 'items'):
        return {k: plain(v) for k, v in value.items()}
    return value


class Network:
    def __init__(self):
        self.queue = []
        self.peers = {}
        for name in ('S', 'A', 'B'):
            lua = LuaRuntime(unpack_returned_tuples=True)
            lua.globals().mode = name
            lua.execute(MOCK)
            lua.globals().sendServerCommand = self.from_server
            lua.globals().sendClientCommand = self.from_client
            lua.execute((LUA / 'shared/B47AHProof.lua').read_text())
            side = 'server/B47AHProofServer.lua' if name == 'S' else 'client/B47AHProofClient.lua'
            lua.execute((LUA / side).read_text())
            self.peers[name] = lua

    def from_server(self, *args):
        if len(args) == 3:
            module, cmd, payload = args
            targets = ('A', 'B')
        else:
            player, module, cmd, payload = args
            targets = (player['name'],)
        for target in targets:
            self.queue.append((target, module, cmd, plain(payload), None))

    def from_client(self, player, module, cmd, payload):
        self.queue.append(('S', module, cmd, plain(payload), player['name']))

    def one(self):
        target, module, cmd, payload, sender = self.queue.pop(0)
        lua = self.peers[target]
        args = lua.table_from(payload, recursive=True)
        if target == 'S':
            lua.globals().emit('OnClientCommand', module, cmd, lua.globals().players[sender], args)
        else:
            lua.globals().emit('OnServerCommand', module, cmd, args)

    def flush(self):
        for _ in range(30):
            if not self.queue:
                return
            self.one()
        raise AssertionError('unbounded command cycle')

    def update(self, count=1):
        for _ in range(count):
            for lua in self.peers.values():
                lua.globals().emit('OnZombieUpdate', lua.globals().Z)

    def arm(self):
        self.peers['A'].globals().B47AHProof.select(7)
        self.flush()
        self.update()

    def set(self, speed):
        self.peers['A'].globals().B47AHProof.set(speed)
        self.flush()

    def sync(self):
        # Nominal native transport mock, not verification of engine packet arithmetic.
        owner = self.peers['S'].globals().Z.owner
        source = self.peers[owner].globals().Z
        for lua in self.peers.values():
            for field in ('walk', 'category', 'scalar'):
                lua.globals().Z[field] = source[field]


class SpeedProofTests(unittest.TestCase):
    def setUp(self):
        self.n = Network()
        self.n.arm()

    def test_mapping_transitions_and_restore(self):
        for speed, category in [('FastShambler', 2), ('Sprinter', 1), ('Shambler', 3)]:
            self.n.set(speed)
            self.assertEqual(self.n.peers['A'].globals().Z.category, category)
            self.assertEqual(self.n.peers['B'].globals().Z.writes, 0)
            self.assertEqual(self.n.peers['S'].globals().Z.writes, 0)
            self.n.sync()
        self.n.peers['A'].globals().B47AHProof.restore()
        self.n.flush()
        self.assertEqual(self.n.peers['A'].globals().Z.scalar, 0.60)
        self.assertEqual(self.n.peers['A'].globals().B47AHProof.ClientState.counts.restores, 1)

    def test_nonadmin_and_invalid_requests(self):
        self.n.peers['B'].globals().B47AHProof.set('Sprinter')
        self.n.flush()
        self.n.set('nonsense')
        self.assertEqual(self.n.peers['A'].globals().Z.writes, 0)

    def test_both_conflict(self):
        self.n.peers['S'].globals().SandboxVars.ZombieLore.ActiveOnly = 2
        self.n.set('Sprinter')
        self.assertEqual(self.n.peers['A'].globals().Z.writes, 0)

    def test_duplicate_and_stale_owner(self):
        self.n.peers['A'].globals().B47AHProof.set('Sprinter')
        self.n.one()  # server dispatch only
        message = self.n.queue[0]
        for lua in self.n.peers.values():
            lua.globals().Z.owner = 'B'
        self.n.update()
        self.n.flush()  # former owner rejects
        self.assertEqual(self.n.peers['A'].globals().Z.writes, 0)
        self.n.set('FastShambler')
        self.assertEqual(self.n.peers['B'].globals().Z.category, 2)
        self.n.queue.append(message)
        self.n.flush()
        self.assertEqual(self.n.peers['A'].globals().Z.writes, 0)

    def test_transfer_restores_server_original(self):
        self.n.set('Sprinter')
        self.n.sync()
        for lua in self.n.peers.values():
            lua.globals().Z.owner = 'B'
        self.n.update()
        self.n.peers['A'].globals().B47AHProof.restore()
        self.n.flush()
        self.assertEqual(self.n.peers['B'].globals().Z.scalar, 0.60)
        self.assertEqual(self.n.peers['B'].globals().Z.category, 3)

    def test_partial_setter_failure_rolls_back(self):
        self.n.peers['A'].globals().Z.failOnce = True
        self.n.set('Sprinter')
        state = self.n.peers['A'].globals().B47AHProof.ClientState
        self.assertTrue(state.rollbackOK)
        self.assertTrue(state.invalid)
        self.assertEqual(self.n.peers['A'].globals().Z.walk, 'slow1')

    def test_scalar_unit_mismatch_blocks(self):
        self.n.peers['A'].globals().Z.scalar = 1000
        self.n.set('Sprinter')
        self.assertEqual(self.n.peers['A'].globals().Z.writes, 0)

    def test_native_drift_never_reapplied(self):
        self.n.set('Sprinter')
        z = self.n.peers['A'].globals().Z
        writes = z.writes
        z.scalar = 0.55
        self.n.update(180)
        self.assertEqual(z.writes, writes)
        self.assertGreater(self.n.peers['A'].globals().B47AHProof.ClientState.counts.drift, 0)

    def test_reused_reference_and_gap_block(self):
        lua = self.n.peers['A']
        lua.execute('Z=newZombie()')
        self.n.update()
        self.n.set('Sprinter')
        self.assertEqual(lua.globals().Z.writes, 0)
        for _ in range(301):
            self.n.peers['S'].globals().emit('OnTick')
        self.assertTrue(self.n.peers['S'].globals().B47AHProof.ServerState.invalid)

    def test_duplicate_live_command(self):
        self.n.peers['A'].globals().B47AHProof.set('Sprinter')
        self.n.one()
        original = self.n.queue[0]
        self.n.queue.append(original)
        self.n.flush()
        self.assertEqual(self.n.peers['A'].globals().Z.writes, 1)

    def test_flat_wire_and_malformed_ack(self):
        self.n.peers['A'].globals().B47AHProof.set('Sprinter')
        self.n.one()
        payload = self.n.queue[0][3]
        self.assertFalse(any(isinstance(v, dict) for v in payload.values()))
        s = self.n.peers['S'].globals().B47AHProof.ServerState
        self.n.queue.clear()
        self.n.queue.append(('S', 'B47AHSpeedProof', 'Ack',
                            {'epoch': s.epoch, 'seq': s.seq, 'ok': True,
                             'resultWalk': 'sprint1', 'resultCategory': 1,
                             'resultScalar': 'bad'}, 'A'))
        self.n.flush()
        self.assertTrue(s.invalid)

    def test_nil_owner_and_single_target(self):
        self.n.peers['S'].globals().Z.owner = None
        self.n.set('Sprinter')
        self.assertEqual(self.n.peers['A'].globals().Z.writes, 0)
        self.n.peers['A'].globals().B47AHProof.select(8)
        self.n.flush()
        self.assertEqual(self.n.peers['S'].globals().B47AHProof.ServerState.id, 7)

    def test_reload_registers_once(self):
        for name, lua in self.n.peers.items():
            side = 'server/B47AHProofServer.lua' if name == 'S' else 'client/B47AHProofClient.lua'
            lua.execute((LUA / side).read_text())
            self.assertEqual(len(lua.globals().Events.OnZombieUpdate.handlers), 1)

    def test_anomalous_scalar_is_observable_without_mutation(self):
        lua = self.n.peers['B']
        lua.globals().Z.scalar = 1000
        self.n.update(60)
        self.assertEqual(lua.globals().B47AHProof.ClientState.samples[1].scalar, 1000)
        self.assertEqual(lua.globals().Z.writes, 0)

    def test_delayed_authorization_ack_is_not_authoritative(self):
        self.n.peers['A'].globals().B47AHProof.set('Sprinter')
        self.n.one()
        # Native authorization stream may lag on A; only server view changes here.
        self.n.peers['S'].globals().Z.owner = 'B'
        self.n.peers['S'].globals().emit('OnZombieUpdate', self.n.peers['S'].globals().Z)
        self.n.flush()
        state = self.n.peers['S'].globals().B47AHProof.ServerState
        self.assertIsNone(state.applied)
        self.assertGreater(state.counts.rejected, 0)
        # This limitation is intentional evidence: old local view can still write.
        self.assertEqual(self.n.peers['A'].globals().Z.writes, 1)

    def test_operator_key_controls(self):
        lua = self.n.peers['A']
        lua.globals().modifiers = True
        lua.globals().emit('OnKeyPressed', 7)
        self.n.flush()
        self.assertEqual(lua.globals().Z.category, 2)
        self.n.sync()
        lua.globals().emit('OnKeyPressed', 10)
        self.n.flush()
        self.assertEqual(lua.globals().Z.scalar, 0.60)


if __name__ == '__main__':
    unittest.main()
