from script_api import *

f = AddByte("Function")

if f == 0: # open portal?
    AddInt("PortalId") # 80005
    AddInt("Unknown") # 39
    AddUnicodeString("Unknown") # s_massive_event_message
    AddUnicodeString("Unknown") # System_Quiz_Global_Portal
    AddUnicodeString("Unknown") # s_massive_event_name_red_arena
    AddUnicodeString("Unknown") # s_massive_event_name_spring_beach
    AddUnicodeString("Unknown") # s_massive_event_name_crazy_runner
elif f == 1: # close portal?
    AddInt("PortalId") # 80005
elif f == 3: # something append message
    pass
elif f == 4: # something append message
    pass
