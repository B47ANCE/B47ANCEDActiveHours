"""Offline compatibility admission only; no native PZ or multiplayer execution."""
from pathlib import Path
import hashlib
import json
import os
import unittest

if os.environ.get('B47_COMPAT_LUA') == '54':
    from lupa.lua54 import LuaRuntime
else:
    from lupa.lua51 import LuaRuntime

ROOT = Path(__file__).resolve().parents[1]
LUA = ROOT / 'src/B47ANCEDActiveHours/42/media/lua/shared'
MOCK = '''
calls={events=0,network=0,mutation=0}
Events=setmetatable({},{__index=function()
 return {Add=function() calls.events=calls.events+1 end}
end})
function sendClientCommand() calls.network=calls.network+1 end
function sendServerCommand() calls.network=calls.network+1 end
function toggleModActive() calls.mutation=calls.mutation+1 end
function isModActive() error('No string overload is assumed') end
function getActivatedMods()
 return {size=function() return #activeIDs end,
         get=function(_,index) return activeIDs[index+1] end}
end
function require(name)
 assert(name=='B47ANCEDActiveHours/Compatibility','Unexpected dependency: '..name)
 return true -- Kahlua-style return: callers must use the populated namespace.
end
'''


class CompatibilityTests(unittest.TestCase):
    def peer(self, ids=('B47ANCEDActiveHours',), prelude=''):
        lua = LuaRuntime(unpack_returned_tuples=True)
        lua.globals().activeIDs = lua.table_from(ids)
        lua.execute(MOCK)
        lua.execute(prelude)
        lua.execute((LUA/'B47ANCEDActiveHours/Compatibility.lua').read_text(encoding='utf-8'))
        lua.execute((LUA/'B47ANCEDActiveHours.lua').read_text(encoding='utf-8'))
        return lua

    def assert_inert(self, lua):
        self.assertEqual(lua.globals().calls.events, 0)
        self.assertEqual(lua.globals().calls.network, 0)
        self.assertEqual(lua.globals().calls.mutation, 0)

    def test_independent_admission_without_framework(self):
        lua = self.peer()
        self.assertTrue(lua.globals().B47ANCEDActiveHours.Enabled)
        self.assertEqual(lua.globals().B47ANCEDActiveHours.Status, 'STANDALONE')
        self.assertIsNone(lua.globals().Mortis)
        self.assert_inert(lua)

    def test_mortis_wins_in_both_load_orders_and_all_peer_fixtures(self):
        for role in ('dedicated mock', 'client A mock', 'client B mock'):
            for ids in (['ProjectMORTIS', 'B47ANCEDActiveHours'], ['B47ANCEDActiveHours', 'ProjectMORTIS']):
                with self.subTest(role=role, ids=ids):
                    lua = self.peer(ids)
                    self.assertFalse(lua.globals().B47ANCEDActiveHours.Enabled)
                    self.assertEqual(lua.globals().B47ANCEDActiveHours.Status, 'MORTIS_ENABLED')
                    self.assertIsNone(lua.globals().Mortis)  # Native list works before its Lua namespace exists.
                    self.assert_inert(lua)

    def test_framework_namespace_is_not_enabled_mod_detection(self):
        lua = self.peer(prelude='Mortis={}')
        self.assertTrue(lua.globals().B47ANCEDActiveHours.Enabled)

    def test_missing_global_fails_closed(self):
        lua = self.peer(prelude='getActivatedMods=nil')
        self.assertFalse(lua.globals().B47ANCEDActiveHours.Enabled)
        self.assertEqual(lua.globals().B47ANCEDActiveHours.Status, 'MOD_LIST_UNAVAILABLE')

    def test_failed_or_nil_lookup_fails_closed(self):
        for body in ("error('unavailable')", 'return nil'):
            lua = self.peer(prelude='function getActivatedMods() '+body+' end')
            self.assertFalse(lua.globals().B47ANCEDActiveHours.Enabled)
            self.assert_inert(lua)

    def test_empty_or_uninitialized_list_fails_closed(self):
        for ids in ([], ['OtherMod']):
            lua = self.peer(ids)
            self.assertFalse(lua.globals().B47ANCEDActiveHours.Enabled)
            self.assertEqual(lua.globals().B47ANCEDActiveHours.Status, 'MOD_LIST_NOT_READY')

    def test_mortis_blocks_even_when_self_is_missing(self):
        lua = self.peer(['ProjectMORTIS'])
        self.assertFalse(lua.globals().B47ANCEDActiveHours.Enabled)
        self.assertEqual(lua.globals().B47ANCEDActiveHours.Status, 'MORTIS_ENABLED')

    def test_invalid_or_unbounded_count_fails_closed(self):
        for count in ('-1', '0', '4097', '1.5', '0/0', 'math.huge', 'true', "'1'"):
            lua = self.peer(prelude='function getActivatedMods() return {size=function() return '+count+' end} end')
            self.assertFalse(lua.globals().B47ANCEDActiveHours.Enabled)
            self.assert_inert(lua)

    def test_bad_size_or_getter_fails_closed(self):
        for definition in ('{}', '{size=function() error("bad") end}',
                           '{size=function() return 1 end}',
                           '{size=function() return 1 end,get=function() error("bad") end}'):
            lua = self.peer(prelude='function getActivatedMods() return '+definition+' end')
            self.assertFalse(lua.globals().B47ANCEDActiveHours.Enabled)
            self.assert_inert(lua)

    def test_malformed_mod_id_fails_closed(self):
        for value in (12, True, '', 'x'*257):
            lua = self.peer(['B47ANCEDActiveHours', value])
            self.assertFalse(lua.globals().B47ANCEDActiveHours.Enabled)

    def test_exact_identity_avoids_false_positive(self):
        lua = self.peer(['B47ANCEDActiveHours', 'ProjectMORTISAddon', 'projectmortis'])
        self.assertTrue(lua.globals().B47ANCEDActiveHours.Enabled)

    def test_entry_gate_rechecks_instead_of_caching_permission(self):
        lua = self.peer()
        lua.globals().activeIDs = lua.table_from(['B47ANCEDActiveHours','ProjectMORTIS'])
        allowed, reason = lua.globals().B47ANCEDActiveHours.canRun()
        self.assertFalse(allowed)
        self.assertEqual(reason, 'MORTIS_ENABLED')
        self.assertFalse(lua.globals().B47ANCEDActiveHours.Enabled)
        self.assert_inert(lua)

    def test_duplicate_load_does_not_register_events(self):
        lua = self.peer(['B47ANCEDActiveHours','ProjectMORTIS'])
        for _ in range(3):
            lua.execute((LUA/'B47ANCEDActiveHours/Compatibility.lua').read_text(encoding='utf-8'))
            lua.execute((LUA/'B47ANCEDActiveHours.lua').read_text(encoding='utf-8'))
        self.assertFalse(lua.globals().B47ANCEDActiveHours.Enabled)
        self.assert_inert(lua)

    def test_build_metadata_and_version_are_independent(self):
        info = dict(line.split('=',1) for line in (ROOT/'src/B47ANCEDActiveHours/42/mod.info').read_text().splitlines() if '=' in line)
        self.assertEqual(info['id'],'B47ANCEDActiveHours')
        self.assertNotIn('require',info)
        self.assertEqual(info['modversion'], (ROOT/'VERSION').read_text().strip())
        self.assertEqual(self.peer().globals().B47ANCEDActiveHours.Version, info['modversion'])
        self.assertTrue((ROOT/'src/B47ANCEDActiveHours/common/.keep').exists())
        for original, copied in (
            ('assets/branding/ActiveHoursClockIcon.png','src/B47ANCEDActiveHours/42/icon.png'),
            ('assets/branding/B47_ICON.png','src/B47ANCEDActiveHours/42/poster.png'),
            ('thumbnail.png','src/B47ANCEDActiveHours/thumbnail.png'),
        ):
            self.assertEqual((ROOT/original).read_bytes(), (ROOT/copied).read_bytes())

    def test_original_diagnostics_artwork_and_publication_are_unchanged(self):
        baseline = json.loads((ROOT/'scripts/standalone-compatibility-preservation.json').read_text())
        for name, digest in baseline.items():
            self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),digest,name)


if __name__ == '__main__':
    unittest.main()
