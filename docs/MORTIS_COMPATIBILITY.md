Project Version: 0.1.0-dev.5

# Standalone Active Hours and built-in MORTIS features

The user's clarification on 2026-10-16 supersedes the retirement interpretation. Active Hours remains maintained as a standalone mod; MORTIS includes the complete Active Hours feature scope within its own mod. The implementations are mutually exclusive, with mandatory MORTIS precedence. This policy has no user override setting because duplicate controllers/writes would invalidate the authority boundary.

| Enabled mods | Standalone Active Hours execution | MORTIS behavior |
|---|---|---|
| Active Hours only | Admitted by the compatibility guard; gameplay still unimplemented | Absent |
| MORTIS only | Absent | Its built-in implementation owns the feature scope |
| Both | Disabled before any future standalone controller registration/writes | MORTIS takes precedence |
| Activated-mod detection unavailable/invalid/not ready | Inactive, fail closed | Never changed by Active Hours |

Current independent source: `src/B47ANCEDActiveHours/42/`, Mod ID `B47ANCEDActiveHours`, `common/` sibling. No MORTIS, Nightfall, experienceWorks or B47ANCEDKnowledgeAndWisdom dependency is declared or imported. This checkpoint implements admission/disable logic only; it does not yet provide speed or solar gameplay. MORTIS likewise currently has an experimental diagnostic rather than completed solar/profile policy. Feature parity is a development requirement, not a runtime verification claim.

## Guard implementation and limits

`media/lua/shared/B47ANCEDActiveHours/Compatibility.lua:check()` protects `getActivatedMods()` and the vanilla list `size()/get(i)` calls. Exact `ProjectMORTIS` presence returns `false, MORTIS_ENABLED` even if the MORTIS Lua namespace has not loaded yet. Merely installed/downloaded artwork or a global named Mortis is not the enabled-mod decision. No `isModActive("id")` overload is assumed; inspected native source takes a mod-info object.

A valid mod list must also contain this standalone ID before an absence of MORTIS authorizes execution. Empty, missing-self, oversized (>4096), noninteger/nonfinite, malformed or failed list observations stay inactive. Limits are internal safety bounds, not gameplay tuning. No Lua table/string-list fallback guesses readiness. Startup timing and exact IDs on the dedicated host remain runtime gates; unknown state never enables a writer.

`media/lua/shared/B47ANCEDActiveHours.lua` calls the guard and exposes `B47ANCEDActiveHours.canRun()`. That entry gate rechecks instead of caching a positive permission; `Enabled` and `Status` are diagnostic results of the latest observation, not proof that gameplay exists. There are currently no event registrations, requests, zombie scans, native setters, profile/controller construction or saved state. Future modules must call the same gate before registration and state-changing entry points. No code is permitted to ignore it or reactivate the standalone controller from a client setting.

Disabling means skipping Active Hours' execution. It does not uncheck a saved mod list, unload other Lua, edit server configuration, remove MORTIS, migrate a save, mutate vanilla sandbox settings or silently change subscriptions. Normal mod-list changes/restarts are human-operated. No hot-mod-toggle or automatic restoration of an already-running future controller is certified. This has no networking protocol: each peer reads the native session list; shared gameplay still requires server authority. Mismatched client/server mod sets are unsupported and need native rejection/disable testing.

## Source evidence

[VERIFIED source, client call] Installed Steam build `25485521`, `media/lua/client/ISUI/ISPauseModListUI.lua:19-21`, calls `getActivatedMods`, then `size` and zero-based `get`. [VERIFIED native inspection] the retained local `research/jar-source/zombie/Lua/LuaManager$GlobalObject.java:3991-3993` declares a global method returning the filesystem mod-ID list. `:3952-3958` shows the object argument to `isModActive`. Read-only native metadata/library evidence identifies `GlobalObject.getActivatedMods():java.util.List`, BCI 0-6, returning `ZomboidFileSystem.getModIDs`. Current JAR and vanilla-source fingerprints are in [evidence/compatibility-25485521.json](evidence/compatibility-25485521.json). No game source/binaries are redistributed or changed.

[INFERRED] The shared global is expected on a dedicated server. No direct dedicated Lua caller, actual server invocation, startup list readiness, Kahlua execution or co-enabled behavior was observed. Full executed game version is UNKNOWN; the target is 42.21 and the installed Steam manifest build is known. API failure closes admission. Offline list mocks demonstrate the Lua branch behavior only.

## Human runtime matrix — NOT TESTED

After independent authorization and reviewed disposable test prerequisites, a human must check standalone-only, MORTIS-only, co-enabled and unavailable/early list scenarios in SP plus one dedicated server with two clients. Record full builds, exact mod lists/versions and each peer's `Enabled`/`Status`. Co-enabled must report MORTIS_ENABLED, zero standalone registrations/requests/writes and normal MORTIS operation, in both available load orders and after reconnect/restart. Do not enable either historical diagnostic as a substitute for the independent source. Do not mark production speed/solar PASS from a compatibility flag. Current source creates no gameplay writers even standalone; future controller tests must count actual writes and verify no duplicated effects.

Future meaningful profile/solar/range options belong in server-authoritative localized sandbox settings. Each implementation owns its namespace and persistence; there is no automatic cross-mod configuration/save migration. MORTIS includes all Active Hours features; this project continues independently. Preserve both Mod IDs, repositories, artwork, Workshop IDs and historical evidence.

G2 BLOCKED, G6 NOT TESTED, G7 BLOCKED / NOT TESTED, G8 BLOCKED. No install, launch, packaging, deployment, upload, retirement or subscriber conversion occurs here.
