from script_api import *

f = AddByte("Function")
if f == 0:
    AddInt("CurrentMapId")
    AddInt("PortalId")
    AddField("Unknown", 10)
    AddUnicodeString("Password") # For locked portals
