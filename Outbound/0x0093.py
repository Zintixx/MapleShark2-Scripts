from script_api import *

f = AddByte("function")

if f == 1:
    # MasteryType = 11, Rank = 2, Reward = 110002
    AddInt("RewardId")
elif f == 2:
    AddInt("RecipeId")
    # RemoveItem/RemoveMoney
    # >> 21 00 02 61 BB 6B EE DE 95 6D 26 E9 1E 00 00
    # >> 3A 00 61 38 26 00 00 00 00 00 23 0C 00 00
    # SendMastery
    # >> CF 00 00 07 20 3E 01 00 00 00 00 00
