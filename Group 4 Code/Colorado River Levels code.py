# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:05:06 2024

@author: Caleb Bowman
"""
import matplotlib.pyplot as plt


crl=open('coloradoriverlevels.txt')

crllines=crl.readlines()

rl=[]
time=[]

for i in range(125,221):
    crldata=crllines[i]
    data=crldata.split()
    for index in range(len(data)):
        columns = crldata.split()
        riverlevel=columns[5]
        times=columns[3]
        rl.append(float(riverlevel))
        time.append(times)
plt.plot(time, rl,color='g')
plt.ylabel("Water Level (ft)")
plt.xlabel("Time (CDT)")
plt.xticks(time[::70],rotation=45)
plt.grid(True)
plt.title("Colorado River at Austin, TX October 31,2013")
        
