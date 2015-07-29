#! /usr/bin/env python
# -*- coding:utf-8 -*-
# 04.py

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.split()

dict = {}
single = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for element in str:
    if str.index(element) + 1 in single:
        dict[element[:1]] = str.index(element) + 1
    else:
        dict[element[:2]] = str.index(element) + 1

for k, v in sorted(dict.items(), key=lambda x:x[1]):
    print k, v