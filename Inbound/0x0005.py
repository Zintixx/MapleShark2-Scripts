''' RECONNECT (sub_0071D460) '''
from script_api import *

f = add_byte("function")
if f == 0:
    add_int("Unknown") # count?
    add_str("SomeKey") # CjhWVm0HAAB2wucC3975500370134093852
    add_int("Unknown")
elif f == 1: # disconnected
    pass
elif f == 2:
    add_int("code") # see: sub_71CD60

"""
bool __stdcall sub_71CD60(int a1)
{
  if ( a1 <= 405 )
  {
    if ( a1 < 400 )
    {
      switch ( a1 )
      {
        case 100:
        case 101:
        case 102:
        case 103:
        case 104:
        case 105:
        case 106:
        case 203:
        case 204:
          return 1;
        default:
          return 0;
      }
    }
    return 1;
  }
  return a1 >= 407 && a1 <= 408;
}
"""