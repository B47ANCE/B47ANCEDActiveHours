# Version inventory

Project Version: 0.1.0-dev.6

Root VERSION is canonical; version-inventory.json declares every current selector. Current runtime mirrors are `src/B47ANCEDActiveHours/42/mod.info` modversion and `src/B47ANCEDActiveHours/42/media/lua/shared/B47ANCEDActiveHours.lua` AH.Version. Current documentation mirrors are the exact Project Version headers inventoried in JSON, including MORTIS_COMPATIBILITY.md, README and the newest CHANGELOG entry. Scripts read canonical VERSION or use synthetic fixtures; source/provenance hashes are not project versions.

Both proof trees and docs/MORTIS_SPEED_PROOF.md are frozen historical dev.3/dev.4, excluded from current mirrors. Dated research/audit/validation bodies, preservation manifests and docs/publications retain their actual versions. Existing dist/current and dist/preview-retry dev.4 packages remain historical, untouched. The old build_mortis_test_package.py tool intentionally refuses the new canonical version because its frozen mod metadata differs; it is not a standalone builder.

Future independent package rule is `dist/standalone-current/B47ANCEDActiveHours-{version}.zip` with embedded `mods/B47ANCEDActiveHours/42/mod.info` and shared AH.Version. Missing output is deferred in development and fails --release. A separate deterministic standalone builder/verifier is now authorized for the existing-item MP test; it has no installer/uploader/restart stage. No stable-release approval is created. Full package-integrity/provenance tooling remains required before packaging. Source inventory is SOURCE_INVENTORY.json.

Target PZ 42.21, Steam build 25485521, MORTIS/dependency versions and API/schema/tool numbers are independent categories. The 0.1.0-dev.5 checkpoint is a compatible new guard capability within unreleased 0.1.0. No production gameplay contract is added; runtime gates are unchanged. No current standalone mirror is intentionally incomplete; future gameplay/configuration/package mirrors do not exist yet and must be inventoried when implemented.

The project-owned docs/MOD_OVERVIEW.json version is a current mirror; its reviewed source_digest is refreshed after source/README/version changes. docs/publications receipts retain their exact uploaded source/versions and are historical, not current mirrors.
