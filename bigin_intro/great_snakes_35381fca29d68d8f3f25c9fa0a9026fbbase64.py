#!/usr/bin/env python3

import sys
import base64
import re
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

print("Here is your flag:")
data = bytes.fromhex('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')
print(base64.b64encode(data))
