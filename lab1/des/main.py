#!/usr/bin/python3

from des import DesKey

key = DesKey(b"some key")

enc = key.encrypt(b"ion dodon", padding=True)

print(enc)
print(key.decrypt(enc))
