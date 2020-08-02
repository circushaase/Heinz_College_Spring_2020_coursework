# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:02:41 2020

@author: Lara
"""
import os
os.chdir('C:/Users/Lara/Documents/DFP/hw2')

# a.
records = []
with open('expenses.txt') as f: 
    lines = [x.rstrip() for x in f]
    for line in lines:
        records.append(line)

for line in records:
    print(line)
        
        
# b.
records2 = []
with open('expenses.txt') as f: 
    lines = [x.rstrip() for x in f]
    records2 = [i for i in lines]
    
print("\nrecords == records2:",records == records2, '\n')

# c.
with open('expenses.txt') as f: 
    lines = [x.rstrip() for x in f]
    records3 = tuple([tuple(i.split(sep=':')) for i in lines])

for tup in records3:
    print(tup)


# d. 
cat_set = {i[1] for i in records3}
cat_set.remove('Category')

date_set = {i[2] for i in records3}
date_set.remove('Date')

print('Categories:', cat_set, '\n')
print('Dates:     ', date_set, '\n')


# e. 
rec_num_to_record = {k:records3[k] for k in range(len(records3))}

for rn in range(len(rec_num_to_record)):
		    print('{:3d}: {}'.format(rn, rec_num_to_record[rn]))


for i in rec_num_to_record.items():
		    print('{:3d}: {}'.format(i[0], i[1]))

for k, v in rec_num_to_record.items():
		    print('{:3d}: {}'.format(k, v))









