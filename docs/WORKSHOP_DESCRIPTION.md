Project Version: 0.1.0-dev.6

# B47ANCE'd Active Hours

## Overview
MP testing build - dedicated multiplayer NOT TESTED

Development compatibility foundation for the standalone Active Hours mod. This build does not implement zombie speed switching, solar progression or other gameplay attributes. It is supplied for controlled loading and compatibility observation, not normal gameplay.

## Features
- Lua-only standalone compatibility gate; no framework dependency.
- Standalone execution is disabled when ProjectMORTIS is enabled. MORTIS takes precedence and includes the Active Hours feature scope.
- Unknown, unavailable or malformed enabled-mod detection stays inactive.
- Transparent day/night alarm-clock mod icon, with the original project and Workshop thumbnail unchanged.
- No zombie writes, automatic mod-list changes, population scans or continuous correction.

## Compatibility & Requirements
Target: Project Zomboid Build 42.21. Native SP/client/dedicated startup and mod-list timing are NOT TESTED. Offline mocks and source inspection do not establish in-game compatibility.

Mod ID: B47ANCEDActiveHours. No MORTIS, experienceWorks or Knowledge & Wisdom dependency. Incompatible with ProjectMORTIS: Active Hours disables its own execution when MORTIS is enabled. This does not disable MORTIS or edit selected mods.

This replaces the item's earlier experimental Mod ID B47ANCEDActiveHoursMortisProof with the independent Core Mod ID. Human operators must update disposable test mod lists explicitly and disable either historical proof; no automatic save/server/subscription conversion occurs. Existing production saves are not validated.

## Configuration
No speed/solar gameplay options or keyboard speed controls exist in this build. The mandatory MORTIS precedence rule has no override setting. Future meaningful gameplay settings remain server-authoritative sandbox settings.

## Source Code & Development
GitHub: https://github.com/B47ANCE/B47ANCEDActiveHours

Research, historical diagnostics, exact evidence limits and the human compatibility matrix remain in the repository. Both historical speed proofs are excluded from this item's new payload. No Java, launcher modifications or native binary changes.

## Known Issues
Compatibility admission only: no production speed/solar controller. Dedicated global availability, mod-list readiness, native co-enabled behavior, reconnect/restart and in-game icon display require human tests. Planned feature parity with MORTIS is not completed gameplay. G2 BLOCKED, G6 NOT TESTED, G7 BLOCKED / NOT TESTED, stable-release G8 BLOCKED. Workshop distribution is not runtime approval.

## Credits & Permissions
Developed by B47ANCE'd Workshop. The user-approved pixel-art clock icon was extracted from the selected project thumbnail using built-in image generation. Original thumbnail and fallback artwork are preserved; no external-mod implementation or assets are bundled.
