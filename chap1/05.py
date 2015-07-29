#! /usr/bin/env python
# -*- coding:utf-8 -*-
# 05.py

original = "I am an NLPer"

def ngram(input, n):
    # 文字 n-gram (引数 str)
    l = len(input)
    if type(input) == str:
        input = "$" * (n - 1) + input + "$" * (n - 1)
        for i in xrange(l + 1):
            print input[i:i+n]
    # 単語 n-gram (引数 list)
    elif type(input) == list:
        input = ["$"] * (n - 1) + input + ["$"] * (n - 1)
        for i in xrange(l + 1):
                print input[i:i+n]

ngram(original, 2)              # 文字 n-gram
original = original.split()
ngram(original, 2)              # 単語 n-gram