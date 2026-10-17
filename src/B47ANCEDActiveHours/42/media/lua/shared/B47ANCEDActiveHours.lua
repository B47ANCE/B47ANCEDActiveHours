require "B47ANCEDActiveHours/Compatibility"
local AH = B47ANCEDActiveHours
AH.Version = "0.1.0-dev.5"

-- Future standalone entry points must use this gate before registering/acting.
-- The current checkpoint contains no speed/solar controller or zombie writer.
function AH.canRun()
    AH.Enabled, AH.Status = AH.Compatibility.check()
    return AH.Enabled, AH.Status
end

AH.canRun()
