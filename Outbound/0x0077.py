from script_api import *

f = AddByte("Function")

if f == 1: # use scroll
    AddLong("ScrollUid")
    AddLong("EquipUid")
    AddField("Unknown 9", 9)
    b = AddBool("UseLock")
    if b:
        AddByte()
        AddShort()
elif f == 3: # select new
    AddLong("EquipUid")
