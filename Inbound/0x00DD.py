from script_api import *
from item import *

f = add_byte("function")

if f == 1: # add item to ui
    add_long("ItemUid")
    add_short("slot")
elif f == 2: # remove item from ui
    add_long("ItemUid")
elif f == 3:
    count = add_byte("count")
    for i in range(count):
        add_long("ItemUid")
        decode_item(0)
elif f == 4:
    add_int("ErrorCode")
