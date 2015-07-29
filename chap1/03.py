#! /usr/bin/env python
# -*- coding:utf-8 -*-
# 03.py

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.replace('.', "")
str = str.replace(',', "")
str = str.split()

list = []

for word in str:
    list.append(len(word))

print list