#! /usr/bin/env python
# -*- coding:utf-8 -*-
# 08.py

str = "Atbash is a simple substitution cipher for the Hebrew alphabet."

def cipher(input):
    ret = ""
    for char in input:
        ret += chr(219-ord(char)) if char.islower() else char
    return ret

str = cipher(str)
print str
str = cipher(str)
print str