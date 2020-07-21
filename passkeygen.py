#!/usr/bin/env python
import random
import string
import pyperclip
passKeyList = []
key = None
charHolder = []
i = 0
while (i < 8):
    charHolder.append(str(random.randint(0,9)))
    charHolder.append(random.choice(string.ascii_letters))
    i = i + 1
random.shuffle(charHolder)
key = "".join(charHolder)
passKeyList.append(key)
# print(passKeyList)
print(f"Thank you for using passkeygen.py your key is: {key}")
i = 0
pyperclip.copy(key)
print("# KEY COPIED TO CLIPBOARD!")