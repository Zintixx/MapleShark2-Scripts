from script_api import *

f = add_byte("function")
if f == 1:
    count = 1
else:
    count = add_int("count")

for i in range(count):
    with Node("Breakable " + str(i), True):
        add_str("EntityId")
        add_byte("Unknown") # 2
        add_byte("Visible?") # 1
        add_int("Unknown")
        add_int("ServerTick")