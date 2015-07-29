#! /usr/bin/env python
# -*- coding:utf-8 -*-
# 07.py

x = 12
y = u'気温'
z = 22.4

def function(x, y, z):
    return unicode(x) + u'時の' + unicode(y) + u'は' + unicode(z)

print function(x, y, z)
