# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:17:34 2024

@author: Caleb Bowman
"""

import matplotlib.pyplot as plt


wcl=open('Willcreeklevels103113.txt')

wcllines=wcl.readlines()

rl=[]
time=[]
date=[]

for i in range(88,365):
    wcldata=wcllines[i]
    data=wcldata.split()
    for index in range(len(data)):
        columns = wcldata.split()
        rainfall=columns[5]
        times=columns[3]
        dates=columns[2]
        rl.append(float(rainfall))
        time.append(times)
        date.append(dates)
plt.plot(time, rl,color='g')
plt.ylabel("Water Level (ft)")
plt.xlabel("Time (CDT)")
plt.xticks(time[::180],rotation=45)
plt.grid(True)
plt.title("Williamson Ck at Jimmy Clay Rd, Austin, TX October 31, 2013 ")