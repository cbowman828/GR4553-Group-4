# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:05:24 2024

@author: Caleb Bowman
"""

import matplotlib.pyplot as plt


walcl=open('walnutcreeklevels103113.txt')

walcllines=walcl.readlines()

rl=[]
time=[]

for i in range(316,603):
    walcldata=walcllines[i]
    data=walcldata.split()
    for index in range(len(data)):
        columns = walcldata.split()
        riverlevel=columns[5]
        times=columns[3]
        rl.append(float(riverlevel))
        time.append(times)
plt.plot(time, rl,color='g')
plt.ylabel("Water Level (ft)")
plt.xlabel("Time (CDT)")
plt.xticks(time[::180],rotation=45)
plt.grid(True)
plt.title("Walnut Ck at Webberville Rd, Austin, TX October 31, 2013 ")