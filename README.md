Project Version: 0.1.0-dev.5

# B47ANCE'd Active Hours

![B47ANCE'd Active Hours project thumbnail](thumbnail.png)

Active Hours remains a maintained standalone mod. M.O.R.T.I.S. will include its complete feature set as a built-in subsystem. The two implementations are incompatible: **when `ProjectMORTIS` is enabled, Active Hours disables its own execution and MORTIS takes precedence.** Neither mod requires the other for this relationship.

## Current development state

The independent source is `src/B47ANCEDActiveHours/`, Mod ID `B47ANCEDActiveHours`. It currently contains a Lua-only compatibility bootstrap, not implemented speed/solar gameplay. It reads activated mod IDs before admitting standalone execution, checks exact `ProjectMORTIS` identity independently of Lua load order, and stays inactive if the list is unavailable, malformed or not ready. It never changes enabled-mod lists, saves, sandbox values or zombie state. Every future gameplay entry point must honor this gate before registering handlers or acting.

[Compatibility contract, evidence and test matrix](docs/MORTIS_COMPATIBILITY.md). The earlier statement that this project was retired/superseded is corrected by the user's clarification. The separate repository, Mod ID, Workshop identity and supplied artwork remain maintained. MORTIS owns its included implementation; this project owns its independent one. Solar progression, Day/Night/Both policy, fixed profiles, weighted ranges and other approved features remain shared development scope; completion/parity is not claimed from design documents.

## Historical diagnostic and Workshop content

Workshop item [3820693462](https://steamcommunity.com/sharedfiles/filedetails/?id=3820693462) still contains the dev.4 **MORTIS-dependent diagnostic**, Mod ID `B47ANCEDActiveHoursMortisProof`. That old test payload is not the new standalone source or an automatically updated item. Both old `proof/` trees remain byte-for-byte historical evidence, including the known owner-routed race in the older experiment. Never install/enable them as the standalone mod or alongside current MORTIS diagnostics. No item/upload/subscriber/save migration is performed here.

MORTIS retains its frozen 64-file dev.4 import for research/history. [Relationship correction](docs/ABSORBED_BY_MORTIS.md), [source inventory](SOURCE_INVENTORY.json), [version inventory](docs/VERSION_INVENTORY.md), [blockers](docs/RELEASE_BLOCKERS.md).

## Development validation

```powershell
python scripts/check_versions.py --root .
python scripts/test_check_versions.py
python scripts/test_standalone_compatibility.py
```

Repeat the last command with `B47_COMPAT_LUA=54` for Lua 5.4; default is Lua 5.1 via development-only lupa. Original diagnostic tests remain available but test their frozen source, not current gameplay. Offline mocks do not prove Kahlua, startup ordering or dedicated MP compatibility.

G2 BLOCKED (production); G6 NOT TESTED; G7 BLOCKED / NOT TESTED; G8 BLOCKED. No game/server launch, install, deploy, package or publish is performed by this checkpoint.

GitHub offline workflow `.github/workflows/offline.yml` checks versions and the compatibility suite under Lua 5.1/5.4, plus frozen prototype regressions under Lua 5.1. It reuses the MORTIS reviewed action pins, read-only token permissions and checkout with credentials not persisted; development-only lupa is pinned to 2.6. No install, deploy, package, upload or native runtime execution. Workflow availability is not branch-protection enforcement.
