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

for i in range(88,365):
    wcldata=wcllines[i]
    data=wcldata.split()
    for index in range(len(data)):
        columns = wcldata.split()
        riverlevel=columns[5]
        times=columns[3]
        rl.append(float(riverlevel))
        time.append(times)
plt.plot(time, rl,color='g')
plt.ylabel("Water Level (ft)")
plt.xlabel("Time (CDT)")
plt.xticks(time[::180],rotation=45)
plt.grid(True)
plt.title("Williamson Ck at Jimmy Clay Rd, Austin, TX October 31, 2013 ")