Project Version: 0.1.0-dev.1

## Versioning initialization — 2026-10-08

User-approved initial version. Development-only checks recorded below; historical validation body remains verbatim. Prior offline source checks remain applicable as retained observations, not runtime proof for this version. No gameplay or research finding changed.

G2 BLOCKED; Phase B NOT STARTED; G6 NOT TESTED; G7 BLOCKED / NOT TESTED; G8 BLOCKED.

[TESTED offline / Python 3.12 bundled development runtime] From the project root, exact commands:

```powershell
& 'C:\Users\willi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/test_check_versions.py
& 'C:\Users\willi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/check_versions.py --root . --json
```

Results: nine integration tests PASS, covering matching, missing canonical, missing mirror, malformed canonical/prerelease, malformed mirror, inconsistent mirror, duplicate selector, missing release artifact and SHA-256 preservation of research/historical audit files. Development checker exits 0 with no errors for canonical 0.1.0-dev.1, fourteen declared current documentation mirrors and newest changelog entry. The missing dist/current/*.zip is reported as deferred, not validated. Temporary fixture --release exits 1 as expected; no archive was generated.

Framework checker copied unchanged from project-template/scripts/check_versions.py; local policy adopts the framework with project-specific version/compatibility decisions. Missing future mod.info/version constants, generated staging and release metadata remain deferred and must enter the inventory before their implementation/packaging. Current documentation mirrors have no inconsistency. Historical unassigned-version statements below remain historical facts; no old evidence was relabeled as runtime validation of this prerelease.

---
Historical validation follows unchanged.

## Lua-only follow-up — 2026-10-08

[TESTED offline] Exact commands from workspace root:

```powershell
& '.\B47ANCE''d Active Hours\research\Check-AuditEvidence.ps1'
& 'C:\Users\willi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' '.\B47ANCE''d Active Hours\research\test_bytecode_index.py'
Get-FileHash -LiteralPath 'E:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\projectzomboid.jar' -Algorithm SHA256
```

Eight existing source assertions plus document presence PASS; five bytecode parser tests PASS. JAR hash remains E1A69EB743EDE60B213A0FE7F8B83D4FCAB773036D256CC4543A336F3B058A33. These validate retained native research, not executable Lua behavior.

Additional inline Python source assertions PASS: Java-style public method exposure exists; each direct category method contains native randomization/helper calls and no DoZombieStats/makeInactive call; six current Lua/solar design documents exist. Source references were checked against retained file paths. No Lua profile code or configuration validator was executed. G2 BLOCKED; Phase B NOT STARTED; G6 NOT TESTED; G7 BLOCKED / NOT TESTED; G8 BLOCKED. No runtime, deployment or packaging occurred; project remains unversioned research.

> CURRENT SCOPE — Lua-only custom behavior profiles supersede native activity control. Retained source evidence is historical and does not prove normal Lua invocation or dedicated multiplayer behavior. See LUA_ONLY_API_AUDIT.md and LUA_MULTIPLAYER_AUTHORITY.md; no runtime gate has passed.

# Audit validation record

2026-10-08, Windows PowerShell, audit-only project with unassigned version.

[TESTED] Offline: CFR extraction/decompilation commands exited 0. These establish inspectable evidence, not engine execution or Lua accessibility. Source review found the overwrite blocker. Decompiled output includes missing-class warnings and is not compilable production code.

Exact decompiler command pattern executed for each extracted class:

```powershell
& 'E:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\jre64\bin\java.exe' -jar '.tmp-nightfall-decompile\cfr-0.152.jar' $dest --outputdir 'True Active Hours\research\jar-source' --silent true
```

The original audit directory was subsequently renamed to `B47ANCE'd Active Hours` following the user's naming instruction. `$dest` was the corresponding class under `True Active Hours\research\jar-classes`; inspected entries are listed by the retained directory inventory and SHA256.json. Extraction used .NET `ZipFile.OpenRead`, `GetEntry` and `ZipFileExtensions.ExtractToFile` against the main game JAR. No base files were modified.

Exact hash verification command executed:

```powershell
Get-FileHash 'E:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\projectzomboid.jar','E:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\zombie\characters\IsoZombie.class' -Algorithm SHA256 | Format-List
```

[TESTED] Offline document check, PASS (four nonempty files):

```powershell
$required=@('README.md','docs\API_AUDIT.md','docs\NATIVE_ACTIVITY_CALL_GRAPH.md','docs\MP_AUTHORITY_AUDIT.md')
foreach($file in $required){
    $p=Join-Path "B47ANCE'd Active Hours" $file
    if(!(Test-Path -LiteralPath $p)){throw "Missing $file"}
    if((Get-Item -LiteralPath $p).Length -eq 0){throw "Empty $file"}
}
```

`Get-ChildItem "B47ANCE'd Active Hours" -Recurse -Filter 'mod.info'` returned no files, consistent with an audit-only result. No gameplay tests were written or executed. `scripts/check_versions.py` is absent in this new audit directory; version validation is BLOCKED pending an established project version and inventory, not PASS. No --release check or packaging occurred.

[RUNTIME GATE] Phase B / G6 client proof: BLOCKED by source architecture. Dedicated multiplayer G7: BLOCKED / NOT TESTED. G8: BLOCKED. Neither PZ nor its server was launched; no live deployment was made.

Before edits, this project directory did not exist. All additions are confined to this directory; SHA256.json records local engine evidence files after extraction. There is no Git baseline in this workspace. No existing project or immutable validation record was rewritten.

## Follow-up investigation, 2026-10-08

[TESTED] Offline source-evidence assertions: exit 0, six assertions and document-presence check passed. Exact command from workspace root:

```powershell
& ".\B47ANCE'd Active Hours\research\Check-AuditEvidence.ps1"
```

These checks verify retained decompiled evidence for build identity, global overwrite, reactivation stats, client registration zero, spawn-event ordering and absence of inactivity in the inspected boolean mapping. They are research consistency checks, not gameplay regression tests or bytecode/runtime verification.

Additional JAR entries extracted and decompiled using the same CFR command with the renamed output directory: zombie/characters/IsoGameCharacter.class, zombie/popman/ZombiePopulationManager.class, zombie/VirtualZombieManager.class. Requested zombie/network/packets/character/ZombieSimulation.class was absent; no conclusion was drawn from that missing guessed path. Additional evidence hashes are recorded separately in research/SHA256-followup.json; the earlier manifest is preserved.

Read-only launcher inspection confirmed configured classpath ordering; launchers were not executed. See NATIVE_BRIDGE_DESIGN.md for the candidate interception and remaining authority/identity/loader prerequisites. No gameplay implementation, native hook verification, Lua invocation, client or dedicated test occurred. G2 remains BLOCKED, G6 NOT TESTED, G7 BLOCKED / NOT TESTED, G8 BLOCKED. Version checker remains blocked pending assigned project SemVer and inventory.

## Expanded handoff attribute audit, 2026-10-08

Baseline JAR SHA256 rechecked unchanged. Additional scoped entries were extracted/decompiled with CFR 0.152: WorldSoundManager, ThumpState, ZombieStateFlags, AttackState, AttackNetworkState, FakeDeadAttackState, animals/AnimalAttackState, ZombieThumpManager, pathfind/PathFindBehavior2, IsoDoor, IsoThumpable and ZombieSimulationPacket. Guessed ZombieAttackState/ZombieAttackNetworkState and vehicles/PathFindBehavior2 entries were absent; enumeration established their actual paths. Missing guessed paths are not evidence of missing capabilities. Additional extracted-class/source hashes are in research/SHA256-attributes.json; earlier manifests retained.

[TESTED] Offline: `& ".\B47ANCE'd Active Hours\research\Check-AuditEvidence.ps1"` exited 0: eight source assertions and document presence passed. The script now checks the full retained DoZombieStats region's observed assignment/call set, absence of toughness initialization there, and door strength/cognition readers. It checks decompiled text, not actual runtime writability or multiplayer correctness.

[TESTED] Offline documentation presence check exited 0 for the ten requested docs. Exact check:

```powershell
$requiredDocs=@('API_AUDIT.md','NATIVE_BRIDGE_FEASIBILITY.md','DYNAMIC_ATTRIBUTES_API_AUDIT.md','ATTRIBUTE_READ_WRITE_CALL_GRAPH.md','ATTRIBUTE_NETWORK_REPLICATION.md','MULTIPLAYER_AUTHORITY.md','PERFORMANCE_DESIGN.md','CONFIGURATION_GUIDE.md','TEST_PLAN.md','RELEASE_BLOCKERS.md')
foreach($doc in $requiredDocs){
    if((Get-Item -LiteralPath (Join-Path "B47ANCE'd Active Hours\docs" $doc)).Length -eq 0){throw "Empty $doc"}
}
```

No production code, config or unsupported option was enabled. Initial version remains unassigned as required by the updated handoff; version checks blocked before implementation. Phase B NOT STARTED; G2 BLOCKED; G6 NOT TESTED; G7 BLOCKED / NOT TESTED; G8 BLOCKED. Runtime proof and Insane performance remain unmeasured. Public loader discovery did not establish the required API, so no loader was adopted. No installed binaries/launchers or external mods were changed.

## Foundational blocker investigation — 2026-10-08

[TESTED offline, Python] Five focused instruction-decoder tests PASS. Whole-JAR selected direct-reference census: 23,829 class files, 247 references, zero parse errors. Both retained updateActiveState variants have identical resolved instructions; raw Code hashes are not compared as semantics because constant-pool indices differ. Source-helper reachability check found no direct getSandboxMemoryDuration invocation. Exact commands from workspace root:

```powershell
& 'C:\Users\willi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' ".\B47ANCE'd Active Hours\research\test_bytecode_index.py"
& 'C:\Users\willi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' ".\B47ANCE'd Active Hours\research\index_attribute_bytecode.py" --jar 'E:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\projectzomboid.jar' --loose-zombie 'E:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\zombie\characters\IsoZombie.class' --output ".\B47ANCE'd Active Hours\research\attribute-bytecode-index.json"
& 'C:\Users\willi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' ".\B47ANCE'd Active Hours\research\summarize_attribute_index.py"
```

These tests verify research tooling/static evidence, not bytecode transformation or PZ execution. Newly identified JAR references were independently decompiled using the earlier CFR command; no third-party gameplay source used. Follow-up includes owner packer/list, command entry points, ECS network component, online-ID allocator, additional attribute readers and reanimation. The indexed appendix gives descriptors/offsets for exact direct references. Reflective/native/bootstrap/mod/agent references remain outside the census.

[VERIFIED documentation] Upstream v2.3.4 documentation/license/API pinned to 9a08a542cfb55f7c8f4973a545639430b3c601ee; no binary downloaded/adopted. Java platform documentation establishes instrumentation/classfile API contracts; installed runtime reports Azul Java 25.0.1 and java.instrument. API module java.compiler is present but compiler module jdk.compiler is absent. No research agent compiled or executed. Earlier statements about missing documented loaders are narrowed by new evidence, not retroactively marked runtime PASS.

No installed binary, launcher or external mod changed; no transformed game class output, production gameplay source, deployment or package created. Project remains unversioned research. G2 BLOCKED; executable Phase B NOT STARTED; G6 NOT TESTED; G7 BLOCKED / NOT TESTED; G8 BLOCKED. ONE_ZOMBIE_POC_ARCHITECTURE.md is conditional research design, not a completed prototype.

Final provenance clarification: “no installed binary changed” above means no installed-file writes by this task. Final read-only hashing detected external loose-class drift from historical A25DFE... to AA340922464B04A9EF12116C0CEBCD9EA5E5DAA33E1B9617A12822BDA839633F. Source/timing UNKNOWN; no assumption of pristine runtime or compatibility. New input bytes were copied only into the research directory under their full SHA256 filename; old source research/manifests remain unchanged. A re-run against the immutable snapshot again parsed 23,829 classes/247 references with zero errors and passed exact seam comparison. Installed class still matched that snapshot on the final read.

Exact final census command uses the snapshot rather than an unstable live input:

```powershell
& 'C:\Users\willi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' ".\B47ANCE'd Active Hours\research\index_attribute_bytecode.py" --jar 'E:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\projectzomboid.jar' --loose-zombie ".\B47ANCE'd Active Hours\research\effective-snapshots\aa340922464b04a9ef12116c0cebcd9ea5e5daa33e1b9617a12822bda839633f.class" --output ".\B47ANCE'd Active Hours\research\attribute-bytecode-index.json"
```

Eight earlier PowerShell source assertions also passed in this turn. SHA256-foundations.json records newly retained JAR classes/decompiler sources; the hash-named index records the effective snapshot. No JVM game class was executed, and no bytecode transform or runtime proof is claimed.
