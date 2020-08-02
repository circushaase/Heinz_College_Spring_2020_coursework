
from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup

html = urlopen('https://www.treasury.gov/resource-center/'
               'data-chart-center/interest-rates/Pages/'
               'TextView.aspx?data=yieldYear&year=2019')

bsyc = BeautifulSoup(html.read(), "lxml")

fout = open('bsyc_temp.txt', 'wt',
		encoding='utf-8')

fout.write(str(bsyc))

fout.close()

# print the first table
#print(str(bsyc.table))
# ... not the one we want
# so get a list of all table tags
table_list = bsyc.findAll('table')

# how many are there?
#print('there are', len(table_list), 'table tags')

# look at the first 50 chars of each table
#for t in table_list:
#    print(str(t)[:50])

# only one class="t-chart" table, so add that
# to findAll as a dictionary attribute
tc_table_list = bsyc.findAll('table',
                      { "class" : "t-chart" } )

# how many are there?
#print(len(tc_table_list), 't-chart tables')

# only 1 t-chart table, so grab it
tc_table = tc_table_list[0]

# what are this table's components/children?
#for c in tc_table.children:
#    print(str(c)[:50])

# tag tr means table row, containing table data
# what are the children of those rows?
#for c in tc_table.children:
#    for r in c.children:
#        print(str(r)[:50])

# we have found the table data!
# just get the contents of each cell

mylist =[]
for c in tc_table.children:
    rowlist = []
    for r in c.children:
        try:
            num = float(r.contents[0])
            rowlist.append(num)
        except:
            rowlist.append(r.contents[0])
    mylist.append(rowlist)
#print(mylist)

fwrt = open('daily_yield_curves.txt', 'wt',
		encoding='utf-8')

for l in mylist:
    q= l[0]
    w= l[1]
    e= l[2]
    r= l[3]
    t= l[4]
    y= l[5]
    u= l[6]
    i= l[7]
    o= l[8]
    p= l[9]
    a= l[10]
    s= l[11]
    d= l[12]
    fwrt.write('{:^10s}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}\n'.format(q,w,e,r,t,y,u,i,o,p,a,s,d))
fwrt.close()




import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date


df= pd.DataFrame(mylist)
new_header = df.iloc[0] 
df = df[1:]
df.columns = new_header

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')



date_set = np.array([x[0] for x in df.values])
#print(x)
x_line =[]
start = pd.to_datetime(date_set[0], format='%m/%d/%y')
for n in date_set:
    dt = pd.to_datetime(n, format='%m/%d/%y')
    delt= (dt-start).days
    x_line.append(delt)
    
y_line = [1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360]

z_line = np.array([x[1:] for x in df.values])
z_line = z_line.astype(float).reshape(250, 12)

ax.plot_surface(x_line, y_line, z_line, rstride=1, cstride=1, cmap='winter', edgecolor='none')
ax.set_title('surface');
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#ax.plot3D(df.columns, y_line, z_line, 'gray')

plt.show()


