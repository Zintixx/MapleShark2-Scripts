from script_api import *
from common import *

f = AddByte("Function")
if f == 0: # improvise start response
    AddInt("InstrumentObjectId")
    AddInt("PlayerObjectId")
    DecodeCoordF("Unknown")
    AddInt("Unknown")
    AddInt("InstrumentType?")
elif f == 3:
    # BROADCASTED: Started playing instrument
    AddByte("Unknown (1)")
    AddInt("InstrumentObjectId")
    AddInt("PlayerObjectId")
    DecodeCoordF("Unknown")
    AddInt("Unknown")
    AddInt("InstrumentType?")
    AddInt("Unknown")
    AddByte("Unknown")
    # 36 4B 40 26 18 00 00 00 00 00 00 00 00
    # C4 D6 41 26 18 00 00 00 00 00 00 00 00
    # 76 35 42 26 00 00 00 00 00 00 00 00 00
    # F6 79 70 26 18 00 00 00 00 00 00 00 00
    AddString("MusicCode")
elif f == 2 or f == 4:
    # BROADCASTED: Stopped/Finished playing instrument
    AddInt("InstrumentObjectId")
    AddInt("PlayerObjectId")
elif f == 8:
    # Create Score response
    AddLong("ItemUid")
    DecodeItem(35100000) # Decode music score item
elif f == 9:
    # Update remaining uses on score (After start playing)
    AddLong("ScoreUid")
    AddInt("Remaining uses")
elif f == 10:
    # View Music
    AddLong("ItemUid")
    AddString("MusicCode")
elif f == 14:
    AddInt("FireworksUnk") # 19986893
