Project Version: 0.1.0-dev.1

# Minimal Lua-only one-zombie proof design

Design only; no executable prototype. Versioned research. G2 BLOCKED; Phase B executable Lua speed proof NOT STARTED; G6 NOT TESTED; G7 BLOCKED / NOT TESTED; G8 BLOCKED. This document does not authorize game/server launch or deployment.

Prepare a dedicated 42.21 server and two clients, one standing continuously loaded zombie, ActiveOnly=Both and a recorded vanilla Speed setting. Record effective runtime provenance, native owner, online/persistent identities, category, walk type, speedMod, running/animation/movement and existing stats calls. Use only normal exposed Lua methods/events; inability to observe required fields safely is a blocker, not permission for reflection.

First prove inert normal-Lua method availability and ownership observations. Then server requests one fixed Sprinter change through supported targeted commands; only the current simulation owner applies it once. Compare server, owner and observer locomotion through ordinary native replication. Repeat Shambler, then connected disable/restoration. Record derived-state leftovers and any randomization. Do not compensate with native activity toggles or per-frame writes.

Repeat native owner transfer between the two clients with a pending decision. Old owner must cease writes and stale decisions must not affect a reused identity. No command schema or retry system is approved before observed ordering. Failure to prove authority/order/restoration keeps G2 BLOCKED. Then measure relevant global Speed settings, native stats recalculation, join/reconnect and reconstruction separately. Solar, weighted distributions and extra attributes are excluded from this first proof.

Acceptance requires measured movement/animation and server/owner/observer agreement, no additional DoZombieStats calls, no native AI disruption, no duplicate category application and safe restoration. An offline assertion or getSpeedType match does not satisfy these requirements. Broad implementation, package metadata, release remain deferred.

## Bounded observation sequence — 2026-10-14

1. Inert baseline: record side, monotonic local sequence/time, valid transport ID, nil-safe owner-player presence, remote predicate, category, walk type, speed scalar, running flag, action/animation state and position through supported getters. Avoid getZombieInfo; it changes debug state and can dereference a null owner. Getter availability must be proven in normal Lua before mutation. No direct instance-field access or reflection. Existing DoZombieStats calls cannot yet be counted through a proven Lua hook: record this instrumentation gap explicitly rather than claiming a zero count.
2. Record pursuit/walking, deliberate obstacle/pathfinding and lunge segments independently before and after each fixed category change. Measure displacement/time and compare running, walk type and animation on owner/server/observer. Matching category is not sufficient. Record exact global Speed option for each independent test; never modify sandbox values at runtime.
3. Confirm registration and native owner authorization before server-directed application. Record command receipt and owner observations separately, without assuming shared clocks or event order. If identity/ownership cannot be verified, defer or reject; no speculative command schema. Apply once only at a proven safe decision boundary.
4. Transfer authority with a pending decision; verify old owner ceases writes, new owner does not duplicate/reroll, and observer remains consistent. Include nil owner and missing-object intervals. Keep the first zombie continuously loaded; broader reuse/reconstruction remain later gates.
5. Reverse profile then attempt connected disable using only verified APIs. IsoZombie overrides the getter to read the normal field, matching the inherited setter; test this narrow candidate without assuming full derived-state restoration. Stop mutation experiments when no safe recovery/restoration path exists; disposal of a test zombie is not evidence of restoration. No production prototype before this blocker is addressed.

[UNKNOWN / RUNTIME GATE] Actual Lua calls, movement, event ordering, restoration and native stats instrumentation. Minimal architecture remains conditional server intent -> verified current owner -> native locomotion replication to observer. This is a diagnostic design, not runnable code or authorization to launch/deploy. All original gates remain unchanged.

## Observer/scalar acceptance refinement

Before any category mutation, measure speedMod on server, owner and observer while a baseline zombie is walking. Compare encoded units/quantization against retained packet paths. If observer scalar appears scaled by 1000 or movement disagrees, stop mutation and capture exact engine build/effective class provenance; do not compensate by writing observer speed. Category/walk-type agreement alone cannot pass the experiment.

Then, only after independent speed safety prerequisites, observe lunger/running propagation and animation across pursuit, pathfinding, lunge and ownership transfer. No approved normal-Lua lunger getter/setter pair has been established; use observable behavior and record telemetry gaps. turnDelta getter on IsoZombie now offers a normal-field snapshot candidate, but packets omit explicit turnDelta/animation fields. Connected restoration and transfer must compare behavior as well as supported getters; no serialized snapshot/identity protocol is approved.

## First diagnostic comparison matrix

[INFERRED experiment design] Before mutation, compare each peer in standing/idle, unobstructed pursuit, obstacle/pathfinding and lunge. In every segment record transport identity, confirmed native owner, getSpeedType/getWalkType/getSpeedMod/isRunning, action/animation state and displacement over a bounded interval. A Lua-only probe has no verified access to predictionType/update-mask fields; do not read Java instance fields or label a Lua trace as a packet capture. Those source conditions guide state selection but are not directly observed by the proposed getters.

Repeat an idle-to-moving-to-idle baseline to look for scalar changes before applying any profile. Unconditional walk-type versus optional speed encoding means matching categories with scalar discontinuity must fail the speed experiment. A scalar getter discrepancy alone is diagnostic: correlate with actual motion and animation; do not assert a live engine defect from source arithmetic.

After owner A -> owner B transfer, the simulator returns before remote parsing for authorized owner IDs, while remote peers parse native locomotion. Record the last remote observation and first confirmed-owner observation separately; no claim that a single simultaneous snapshot establishes ordering. Baseline mismatch stops mutation. Passing baseline still does not resolve command timing, stale identity or restoration gates. No executable probe, custom schema or deployment is introduced.

## Read-only observation architecture before mutation

[INFERRED design] First diagnostic slice is local, read-only, with no commands or speed setters. Select one continuously loaded outdoor standing zombie during an explicitly authorized future test; bind a local object reference plus its observed online ID independently on each peer. Object reference is a temporary filter, not server-assigned identity or a durable generation token. A changed ID, dead/crawling state, lost selection or unexplained callback gap invalidates diagnostic coverage and blocks mutation. Do not automatically bind a replacement with the same transport ID.

OnZombieUpdate may supply candidate objects on each side. Filter unwanted callbacks with a constant-time reference/ID check; only the selected object gets bounded sampled getter records. No per-callback serialization/logging for the population, no global traversal, no gameplay values hardcoded by this design. Log only public diagnostic scalars/state and local sequence, never usernames/connection details. Callback overhead still scales with native population; measure it before claiming Insane readiness.

Server indoor early returns mean the first test uses an outdoor zombie and explicitly records event gaps; absence is not lifecycle evidence. Do not query getZombieInfo or shouldSprint, both have source-observed side effects. No prediction-mask, lunger or native stats-call counter is assumed available to ordinary Lua. Existing state/movement acceptance uses only individually audited getters, whose actual Lua invocation is still NOT TESTED.

Read-only baseline may be designed independently of mutation; it does not resolve complete recovery/restoration and authority gates. Targeted server sends may silently drop on missing player mapping/connection. Before a future mutation experiment, prove connected route, current owner and native-state confirmation; never broaden to observers/broadcast as fallback. No command schema, retry logic, persistent identity or executable probe is introduced here.
