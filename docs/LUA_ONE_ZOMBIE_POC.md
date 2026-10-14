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
