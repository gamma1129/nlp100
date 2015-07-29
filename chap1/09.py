#! /usr/bin/env python
# -*- coding:utf-8 -*-
# 09.py
import random

str = "I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = str.split()
shuffled_list = []

for word in words:
    if len(word) < 4:
        pass
    else:
        char_list = list(word)
        mid_list = char_list[1:-1]
        random.shuffle(mid_list)
        word = word[0] + "".join(mid_list) + word[-1]
    shuffled_list.append(word)

shuffled_str = " ".join(shuffled_list)
print shuffled_str