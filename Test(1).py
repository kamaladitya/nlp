#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:37:29 2019

@author: vishesh
"""

from langdetect import detect

print(detect("चुनाव आयोग पहुंचे नेताओं में कांग्रेस के गुलाम नबी आजाद"))

print("\n")

print(detect("A quick brown fox jumped over the lazy dog"))