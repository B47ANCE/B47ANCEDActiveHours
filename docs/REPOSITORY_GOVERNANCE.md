Project Version: 0.1.0-dev.2

# Repository governance

Canonical project version: root VERSION. This is documentation-only research at the canonical development version; onboarding does not change gameplay compatibility or justify a version bump.

Public repository: https://github.com/B47ANCE/B47ANCEDActiveHours

Authoritative current surfaces: README.md, docs/, VERSION, version-inventory.json, CHANGELOG.md and development scripts/. Isolated experimental runtime source and mod.info now exist under proof/B47ANCEDActiveHoursSpeedProof; production modules have no runtime source or metadata. Planned Mod IDs are B47ANCEDActiveHours, B47ANCEDActiveHoursNight and B47ANCEDActiveHoursDay; no Workshop ID is assigned. No package, staging or installed mod is authoritative here.

Local research/ contains engine extractions, decompilation and provenance used by the audits. It remains ignored and unchanged, and is not distributed through GitHub. Source references in the public documents require access to the independently obtained local evidence. Hashes alone do not reconstruct that evidence. No game code or custom Java component is shipped.

Validation: `python scripts/check_versions.py --root .` and `python scripts/test_check_versions.py`. The preservation test checks local research where available; a public checkout can validate preserved historical documents without engine evidence. Missing local evidence is reported, never considered source/runtime proof. Packaging remains deferred and --release fails without required artifacts.

Initial main is the imported research baseline. Further work uses named feature branches and PRs. No stable tag or automatic deployment/publication. G2 BLOCKED; Phase B NOT STARTED; G6 NOT TESTED; G7 BLOCKED / NOT TESTED; G8 BLOCKED. Public GitHub backup is not dedicated multiplayer validation. CI and branch protection have not been configured by this onboarding.

Authoritative isolated runtime source root: proof/B47ANCEDActiveHoursSpeedProof/42/. Diagnostic Mod ID B47ANCEDActiveHoursSpeedProof, no Workshop ID. Added development command: python scripts/test_speed_proof.py (lupa required only offline). No generated outputs, archives or install tree were created.
