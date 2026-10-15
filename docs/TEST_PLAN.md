Project Version: 0.1.0-dev.2

# Current Lua-only validation plan

LUA_ONE_ZOMBIE_POC.md replaces the loader/native-toggle experiment described historically below. First validate fixed speed through normal Lua on one continuously loaded zombie, dedicated server and two clients: owner-only application, native observer replication, true movement/animation, reverse transition, restoration, all relevant global Speed settings, native stats resets and authority handoff. Record exact effective peer provenance and sequence timestamps. No solar or extra attributes in the first proof.

Then test registration delay, stale/reused online IDs, join/reconnect, relevance, virtualization/reconstruction/restart and server-only ownership before wider gameplay. Existing offline assertions remain historical source tests; no Lua profile implementation is tested. G2 BLOCKED; Phase B NOT STARTED; G6 NOT TESTED; G7 BLOCKED / NOT TESTED; G8 BLOCKED. No launch/deployment authorization is implied.

---
Historical test plan follows; interception and native transition experiments are superseded.

# Test plan

No runnable gameplay exists. G2 BLOCKED; Phase B NOT STARTED; G6 NOT TESTED; G7 BLOCKED / NOT TESTED; G8 BLOCKED. This plan does not authorize launch or deployment.

After supported loader/identity/transport proof, test one zombie on a dedicated 42.21 server with two clients: record baseline, server threshold, activate/deactivate under Night and Day, observe native updates and ownership transfer. Test one attribute at a time, then restoration, overwrite timing, damage semantics, reconstruction and network agreement. Native transition counters must show no duplicate toggles or extra DoZombieStats calls.

Before gameplay activation, offline configuration tests must cover Core only, each module, both modules, missing dependency, all vanilla ActiveOnly values, warning suppression with enforcement retained, malformed files, unknown enums, unsupported attributes, fixed/ranged precedence, one-category weights, proportional two-category 20/40, zero/zero, three-category 10/40 -> 10/50/40, reversed range, negative/over-100/nonfinite weights and tolerance-aware totals. No configuration implementation is yet under test.

Runtime matrix: early/mid/late dusk and dawn, endpoints, seasons, endless/degenerate solar modes, storms/indoors/artificial lights, mid-transition spawn, unload/reconstruction, restart, join/reconnect, reuse and ownership changes. Test Both policy with Active profile and coordinated disable/restoration. Verify no hidden client policy or attribute divergence.

Insane population acceptance requires PERFORMANCE_DESIGN.md measurements, stress tests and native/multiplayer correctness. Offline mocks cannot satisfy G6 or G7. Version must be assigned before implementation and recorded in each actual runtime test.

The foundational prototype entry sequence is now specified in ONE_ZOMBIE_POC_ARCHITECTURE.md. Offline evidence tooling checks bytecode instruction alignment and both retained activity seams, but no transform was executed. Future research-transform tests must include unknown/no-match descriptors, duplicate registration, later-agent changes, helper linkage, unchanged makeInactive and every unrelated method. First runtime pass remains inert, then connected disable/restoration, then one activity decision; attributes are separate later experiments. No current runtime gate is PASS.

## Isolated speed-source validation

Run python scripts/test_speed_proof.py (development lupa dependency). Sixteen actual-Lua mock tests cover command trust, nominal owner/observer behavior, category mapping, connected field restoration, transfer, duplicates, failures, anomalies, drift and hotkeys. Delayed-authority test intentionally demonstrates the unresolved old-owner local-write limitation. Dedicated Shambler -> Fast Shambler -> Sprinter -> Shambler, overwrite, handoff and behavioral restoration instructions are in ISOLATED_SPEED_PROOF.md. Mocks do not satisfy G2/G6/G7/G8.
