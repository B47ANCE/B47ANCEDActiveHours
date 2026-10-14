Project Version: 0.1.0-dev.1

# Lua multiplayer authority feasibility

All references below are retained CFR files under `research/jar-source/`. [VERIFIED source] means source inspection only. Full native ordering evidence remains in NATIVE_OWNERSHIP_ORDERING.md and MULTIPLAYER_AUTHORITY.md; their interception proposals are superseded.

1. `zombie/VirtualZombieManager.java:249` fires OnZombieCreate before online ID assignment `:257`, map insertion `:265` and persistent registration `:267`. Do not dispatch a decision from this callback assuming usable network identity.
2. `zombie/popman/NetworkZombieManager.java:87` evaluates authority; moveZombie `:165` changes owner associations. `zombie/popman/NetworkZombiePacker.java:142` postupdate invokes authority processing `:184` before per-peer authorization and synchronization. Transport ID allocation wraps (`zombie/network/IsoObjectID.java:61`); it is not a permanent zombie key.
3. `zombie/network/packets/character/ZombieListPacket.java:34` updates authorization lists. `zombie/popman/NetworkZombieSimulator.java:154` becomes local, `:162` becomes remote. parseZombie `:194` may reconstruct a missing zombie; `:288` returns for an authorized owner before remote-state application. Ownership is not inferred merely from object existence.
4. `zombie/popman/NetworkZombiePacker.java:100` validates incoming sender against current owner `:111`; applyZombie `:240` accepts owner locomotion. Thus server writes alone cannot establish lasting authoritative speed. `zombie/characters/NetworkZombieAI.java:211` serializes locomotion and `:270` applies it on remote peers.
5. Lua transport entry points exist: `zombie/Lua/LuaManager$GlobalObject.java:5180` targeted sendServerCommand; `zombie/network/GameServer.java:3530` resolves player connection. Client reception `zombie/network/GameClient.java:1141` fires OnServerCommand. Client commands `GameClient:1891` are bound to the sending connection/player by `GameServer:2351`. These establish supported transport, not ordering with native authorization packets.

[UNKNOWN / BLOCKED] Command event timing relative to native owner changes; safe pending-decision resolution after registration; normal Lua owner method/connection usability; stale decision rejection across ID reuse; retries/acknowledgment without duplicate rerolls; server-side ownership; join/reconnect snapshots; persistent identity across virtualization/restart. No packet schema is invented while these remain unresolved.

[INFERRED conditional route] Server chooses fixed category, addresses current owner through verified player-targeted Lua commands, and owner checks current native authority immediately before one application. Server confirms owner-produced native state; observer receives normal locomotion packet. A future decision must be invalidated by owner/identity changes, but a reliable generation model has not been proven. Clients cannot submit category choices or self-assign thresholds. Server rejects mismatched sender/identity/authority intent.

First proof is deliberately one continuously loaded zombie with two clients. Handoff is still required, followed by join/reconnect, relevancy loss, virtualization, reconstruction, reuse and restart before general gameplay approval. No server/client has been launched; dedicated multiplayer correctness is NOT TESTED.

## Owner observation refinement — 2026-10-14

[VERIFIED source] IsoZombie.java:635 delegates isRemoteZombie to inherited isRemote. IsoGameCharacter.java:13640 has a false fallback if no NetworkComponent is present; component/NetworkZombieComponent.java:25-26 reports remote when authOwner is null. Simulator becomeLocal sets connection/player, while becomeRemote clears them (NetworkZombieSimulator.java:154-174). Therefore not-isRemote alone is insufficient evidence of fully initialized, current ownership. Server-null ownership must not be interpreted using a client-local predicate.

[UNKNOWN] Supported Lua combination that proves current owner, registered identity and post-authorization readiness. getOwnerPlayer returns an exposed IsoPlayer candidate, but routing/split-screen/transfer semantics need observation. Do not change native ownership. Owner changes between command receipt and application require rejection/defer behavior; no command format or generation protocol is approved here.

[VERIFIED source] LuaManager$GlobalObject.java:4637-4658 getZombieInfo dereferences zombie.getOwner at :4656 without a null-owner guard and sets networkAi.debugInterfaceActive=true at :4657. It is not passive null-safe telemetry and is excluded from the first proof. Public getOnlineID, getSpeedType, getWalkType, getSpeedMod, isRunning, getActionStateName and getAnimationStateName are narrower observation candidates (IsoGameCharacter.java:3771, :12366, :13255, :13259); actual normal-Lua execution remains UNKNOWN. Read owner player only with nil checks; do not log usernames, connection contents or private player data.

## Replication scope refinement — 2026-10-14

[VERIFIED source] Native boolean mapping carries lunger and running. Speed scalar is encoded as thousandths by owner and divided on server; retained remote AI parser instead passes the short directly to the scalar setter. This is a source-level unit discrepancy, not verified runtime behavior. The first proof must establish observer baseline units and actual motion before mutation; do not add independent observer writers. Packet fields do not explicitly carry normal turnDelta, walkVariant or animation-rate state. Vanilla replication offers a candidate path, not complete profile synchronization proof. See LUA_SPEED_CONTROL.md for exact references and limitations.
