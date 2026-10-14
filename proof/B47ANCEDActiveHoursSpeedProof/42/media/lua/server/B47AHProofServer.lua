require "B47AHProof"
if not isServer() then return end
local P = B47AHProof
if P.ServerState then return end
local s = P.newState()
P.ServerState = s
local function reject() s.counts.rejected=s.counts.rejected+1 end
local function admin(player)
    local ok, result = pcall(function() return string.lower(player:getAccessLevel()) == "admin" end)
    return ok and result
end
local function reply(player, command, args) sendServerCommand(player,P.Module,command,args) end
local function observe(z)
    if not P.bind(s,z) then return end
    local ok, owner = pcall(function() return z:getOwnerPlayer() end)
    if not ok then s.invalid=true; return end
    if s.owner ~= owner then
        s.owner=owner; s.pending=nil; s.seq=s.seq+1
        s.counts.ownerChanges=s.counts.ownerChanges+1
    end
    P.sample(s,z)
    if s.expected and s.counts.updates % 60 == 0 then
        if P.matches(P.snapshot(z),s.expected) then
            s.counts.nativeMatches=(s.counts.nativeMatches or 0)+1
        else s.counts.nativeMismatch=(s.counts.nativeMismatch or 0)+1 end
    end
end
local function command(module, cmd, player, args)
    if module ~= P.Module then return end
    if type(args) ~= "table" or not player then reject(); return end
    if cmd == "Ack" then
        if not s.z or s.invalid or not s.pending or args.epoch ~= s.epoch or args.seq ~= s.seq then reject(); return end
        if not P.usable(s.z,s.id) or P.nativeOwner(s.z) ~= player or s.pending.owner ~= player then reject(); return end
        if args.ok == true and P.matches(P.unpackSnapshot(args,"result"),s.pending.value) then
            s.applied=s.pending.kind ~= "Restore"; s.expected=s.pending.value
            if s.pending.kind == "Restore" then s.counts.restores=s.counts.restores+1 end
        else s.counts.errors=s.counts.errors+1; s.invalid=true end
        s.pending=nil
        return
    end
    if not admin(player) then reject(); return end
    if cmd == "Dump" then P.dumpState(s); return end
    if not P.both() then reject(); return end
    if cmd == "Select" then
        -- Never replace an existing test target, including an unacknowledged write.
        if s.id or not P.integer(args.id,0,32767) then reject(); return end
        s.id=args.id; s.epoch=s.epoch+1
        sendServerCommand(P.Module,"Arm",{id=s.id,epoch=s.epoch}) -- Enrollment only; no mutation broadcast.
        return
    end
    if cmd ~= "Set" and cmd ~= "Restore" then reject(); return end
    if s.invalid or not s.z or not P.usable(s.z,s.id) or s.tick-s.last > P.GapTicks or s.pending then reject(); return end
    local owner=P.nativeOwner(s.z)
    if not owner then reject(); return end -- No owner route; never fall back to broadcast/server writes.
    local now=P.snapshot(s.z)
    if not P.valid(now) then reject(); return end
    local value
    if cmd == "Set" then
        value=P.Fixed[args.speed]
        if not value then reject(); return end
        if not s.baseline then s.baseline={walk=now.walk,category=now.category,scalar=now.scalar} end
    else
        value=s.baseline
        if not value then reject(); return end
    end
    s.seq=s.seq+1
    s.pending={owner=owner,value=value,kind=cmd}
    reply(owner,"Apply",{id=s.id,epoch=s.epoch,seq=s.seq,kind=cmd,
        valueWalk=value.walk,valueCategory=value.category,valueScalar=value.scalar,
        expectedWalk=now.walk,expectedCategory=now.category,expectedScalar=now.scalar})
end
Events.OnZombieUpdate.Add(observe)
Events.OnTick.Add(function() P.advance(s) end)
Events.OnClientCommand.Add(command)
