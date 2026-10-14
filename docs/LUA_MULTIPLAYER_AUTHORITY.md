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
