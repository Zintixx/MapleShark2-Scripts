from script_api import *

AddByte("state") # 0x00 = success, 0x07 = restricted, 0x19 = timed out
AddInt("Unknown")
AddUnicodeString("BanReason")
AddLong("AccountId")
AddLong("SyncTime")
AddInt("SyncTicks")
AddByte("TimeZone")
f = AddByte("function")
AddInt("CONST (0)")
AddLong("CONST (0)")
if f == 1:
    AddLong("Timestamp")
elif f == 2:
    AddLong("Timestamps")
    AddLong("CurrentTimestamp")
AddInt("2 (CONST)")
