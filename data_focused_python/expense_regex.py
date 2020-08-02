# -*- coding: utf-8 -*-
"""
Lara Haase (Lhaase)
Data Focused Python - Homework 5

"""

import re

records = []

with open('expenses.txt') as f:
    for line in f:
        line = line.rstrip()
        records.append(line)


# 1a
#pat = r'D'

# 1b
#pat = r'\''

# 1c
#pat = r'\"'

# 1d
#pat = r'^7'

# 1e
#pat = r'[rt]$'

# 1f
#pat = r'\.'

# 1g
#pat = r'r.*g'

# 1h
#pat = r'[A-Z][A-Z]'

# 1i
#pat = r','
        
# 1j
#pat = r'(,.*){3,}'

# 1k
#pat = r'^[^vwxyz]*$'

# 1l
#pat = r'^[1-9]\d\.\d' #\d  = [0-9]

# 1m
#pat = r'^([^,]*,[^,]*){3}$'

# 1n
#pat = r'\('

# 1o
#pat = r'^[1-9]\d\d\.\d\d:meal'  # \d =[0-9]

# 1p
pat = r'^.*:....:.*:'

# 1q
#pat = r'^.*:\d\d\d\d03\d\d:'

# 1r
#pat = r'a.*b.*c'

# 1s
#pat = r'(..).*\1.*\1'

# 1t
#pat = r'^.*:.*:.*:.*(?=.*a)(?=.*[0-9]).*$'

# 1u
#pat = r'^[^A-Z]*$'      

# 1v
#pat = r'^.*d.?i.*$'


for line in records:
    if re.search(pat, line) != None:
        print(line)
     