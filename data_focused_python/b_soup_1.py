# -*- coding: utf-8 -*-

"""
Team 9
Coded by Bairui Zhang (bairuiz) and Lara Haase (Lhaase)
"""
import urllib.request
import bs4
import numpy as np
from datetime import date
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import pandas as pd

html = urllib.request.urlopen('https://www.treasury.gov/resource-center/'
                              'data-chart-center/interest-rates/Pages/'
                              'TextView.aspx?data=yieldYear&year=2019')

bsyc = bs4.BeautifulSoup(html.read(), features="html")

fout = open('bsyc_temp.txt', 'wt',
            encoding='utf-8')

fout.write(str(bsyc))

fout.close()

# so get a list of all table tags
table_list = bsyc.findAll('table')

# only one class="t-chart" table, so add that
# to findAll as a dictionary attribute
tc_table_list = bsyc.findAll('table',
                             {"class": "t-chart"})

# only 1 t-chart table, so grab it
tc_table = tc_table_list[0]

# we have found the table data!
# just get the contents of each cell
daily_yield_curves_list = []

for c in tc_table.children:
    for r in c.children:
        # print(r.contents)
        daily_yield_curves_list.append(r.contents)

np_list = np.array(daily_yield_curves_list)
daily_yield_curves_np_list = np_list.reshape(251, 13)
print(daily_yield_curves_np_list)

month_day_year = []

for dat in daily_yield_curves_np_list[1:, 0]:
    month_day_year_instant = []
    for s in str(dat).split('/'):
        month_day_year_instant.append(int(s))
    time = date(2019, month_day_year_instant[0], month_day_year_instant[1]) - date(2019, 1, 2)
    month_day_year.append(time.days)

# part2

fig = plt.figure()
ax = mplot3d.Axes3D(fig)
X = np.array(month_day_year)
Y = np.array([1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360])
X, Y = np.meshgrid(X, Y)
Z = daily_yield_curves_np_list[1:, 1:].astype(float).T
ax.set_xlabel('Days since 01/02/2019')
ax.set_ylabel('Months to maturity')
ax.set_zlabel('Rate')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
ax.contour(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
ax.set_zlim(-2, 2)
plt.show()

ax1 = plt.axes(projection='3d')
ax1.plot_wireframe(X, Y, Z, color='blue')
ax1.set_title('wireframe');
ax1.set_xlabel('Days since 01/02/2019')
ax1.set_ylabel('Months to maturity')
ax1.set_zlabel('Rate');
plt.show()


# part3
yield_curve_df = pd.DataFrame(daily_yield_curves_np_list[1:, 1:].astype(float), index=daily_yield_curves_np_list[1:, 0],
                              columns=list(daily_yield_curves_np_list[0, 1:]))
yield_curve_df.transpose()
print(yield_curve_df)
yield_curve_df.plot()
plt.show()

# 2
daily_yield_curves_interval = []
daily_yield_curves_interval.append(daily_yield_curves_np_list[0])
i = 0
for data in daily_yield_curves_np_list[1:, ]:
    if i % 20 == 0:
        daily_yield_curves_interval.append(data)
    i += 1
daily_yield_curves_interval_np = np.array(daily_yield_curves_interval)
by_day_yield_curve_df = pd.DataFrame(daily_yield_curves_interval_np[1:, 1:].astype(float).T,
                                     index=[1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360],
                                     columns=list(daily_yield_curves_interval_np[1:, 0]))
by_day_yield_curve_df.plot()
plt.show()
