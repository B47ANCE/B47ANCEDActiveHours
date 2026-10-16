-- Read-only compatibility detection. No engine mutation, events or mod-list writes.
B47ANCEDActiveHours = B47ANCEDActiveHours or {}
local AH = B47ANCEDActiveHours
AH.Compatibility = AH.Compatibility or {}
local C = AH.Compatibility
local MAX_MODS = 4096 -- Internal bound for detection, not a gameplay setting.

function C.check()
    if type(getActivatedMods) ~= "function" then return false, "MOD_LIST_UNAVAILABLE" end
    local ok, mods = pcall(getActivatedMods)
    if not ok or mods == nil then return false, "MOD_LIST_UNAVAILABLE" end
    local read, count = pcall(function() return mods:size() end)
    if not read or type(count) ~= "number" or count ~= count
        or count < 1 or count > MAX_MODS or count ~= math.floor(count) then
        return false, "MOD_LIST_NOT_READY"
    end
    local selfPresent = false
    for index = 0, count - 1 do
        local got, id = pcall(function() return mods:get(index) end)
        if not got or type(id) ~= "string" or id == "" or #id > 256 then
            return false, "MOD_LIST_INVALID"
        end
        if id == "ProjectMORTIS" then return false, "MORTIS_ENABLED" end
        if id == "B47ANCEDActiveHours" then selfPresent = true end
    end
    if not selfPresent then return false, "MOD_LIST_NOT_READY" end
    return true, "STANDALONE"
end

return C
