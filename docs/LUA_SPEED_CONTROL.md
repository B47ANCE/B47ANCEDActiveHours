Project Version: 0.1.0-dev.1

# Lua speed control feasibility

Status: [VERIFIED source-supported candidates], [UNKNOWN runtime safety], [BLOCKED gameplay adapter]. References are retained `research/jar-source/` lines; no speed call has run in PZ.

| Method | Native effects | Limit |
|---|---|---|
| IsoZombie.doZombieSpeed(int), `zombie/characters/IsoZombie.java:4854` | Calls selector `:4858`; handles crawling and selects categories. | Global Speed=3 forces Shambler; global Speed=1/2 also participates. Explicit input alone does not isolate profile. |
| doSprinter(), `:4880` | Sets lunger, random speedMod, walk variant, animation frame speed and category; helper `:4938` sets sprint walkType and turnDelta. | Each call rerolls derived speed. Must not invoke each update. |
| doFastShambler(), `:4891` | Random speedMod, walk variant, animation rate, category and slow walkType. | Does not restore all sprinter-derived state. |
| doShambler(), `:4920` | Random speedMod, walk variant, animation rate, category and slow walkType. | Does not reset lunger or prior sprinter turnDelta. Reversible profile behavior not proven. |
| getSpeedType(), `:4930`; getWalkType(), `:5055` | Read category/walk type. | Category agreement alone does not prove movement/animation correctness. |
| IsoGameCharacter.setSpeedMod(), `zombie/characters/IsoGameCharacter.java:3775` | Sets a scalar. | Does not establish a full category adapter. |

[VERIFIED source] Direct category methods do not call DoZombieStats or makeInactive. Their own random speed/animation writes still occur. `DoZombieStats` (`IsoZombie:3327`, speed call `:3367`) can overwrite a profile at construction, load, reuse, crawl changes and native reconstruction. Existing ATTRIBUTE_READ_WRITE_CALL_GRAPH.md preserves exact caller evidence. ActiveOnly=Both avoids intentional native daily inactivity transitions; it does not prevent other stats resets.

[VERIFIED source] Locomotion still reads global Speed: IsoZombie `:3154` walking speed and `:3172` lunge; `zombie/pathfind/PathFindBehavior2.java:906`, `:985`, `:1015` path movement. Thus the required ActiveOnly=Both prerequisite is insufficient to establish category control under every vanilla Speed option. Test all options; a candidate Random baseline is [INFERRED], not an approved prerequisite or automatic configuration change.

[VERIFIED source] `zombie/characters/NetworkZombieAI.java:211` serializes speedMod/walkType; `:270` parses remote state. `zombie/popman/NetworkZombiePacker.java:240` applies owner data on server, including speedMod `:256` and walkType/derived category `:274`. A server-only mutation may be overwritten. Owner-side mutation has a native observer propagation path, but actual propagation, running flags and animation agreement are [UNKNOWN].

Ten proof questions remain: normal Lua invocation; actual movement; animation/walk type; native overwrite timing; network overwrite timing; observer propagation; ownership transfer; virtualization/reconstruction; faithful disable restoration without extra rerolls; bounded application cost. No category-only observation can close these questions.

Smallest candidate: one standing, continuously loaded zombie, fixed Sprinter/Shambler decisions from server, applied once per accepted decision by its verified simulation owner. Observe ordinary native propagation. No crawler, solar, weighted sampling or additional attribute logic in that first experiment. Connected disable restoration is mandatory and currently [BLOCKED]: restoring only an old category invokes randomization and misses derived state. Do not promise exact restoration or reapply every frame to conceal overwrites.
