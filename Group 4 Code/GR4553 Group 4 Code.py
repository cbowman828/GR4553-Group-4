# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:35:41 2024

@author: buske
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.feature as cf
import cartopy.crs as ccrs
import pygrib
from metpy.io import parse_wpc_surface_bulletin
from metpy.plots import (ColdFront, OccludedFront, StationaryFront, StationPlot, WarmFront)
from metpy.calc import azimuth_range_to_lat_lon
from metpy.cbook import get_test_data
from metpy.io import Level2File
from metpy.plots import add_metpy_logo, add_timestamp, USCOUNTIES
from metpy.units import units

#Synoptic Data

d00Z=pygrib.open('nam_218_20131031_0000_000.grb2')
d12Z=pygrib.open('nam_218_20131031_1200_000.grb2')

#300MB 00Z Synoptic Map (Heights/Winds)

fig=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-120.,-70.,20.,50.])
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES, alpha=0.5)

gl=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False

gph30000Z=d00Z[117]
gph300v00Z=gph30000Z['values']

uwnd30000Z=d00Z[120]
uwnd300v00Z=uwnd30000Z['values']

vwnd30000Z=d00Z[121]
vwnd300v00Z=vwnd30000Z['values']

lats,lons=gph30000Z.latlons()

plt.contour(lons,lats,gph300v00Z,np.arange(8000,10000,100), linewidths=2, colors='black',transform=ccrs.PlateCarree())

bounds300=[30,40,60,80,100,125,150,175,200]
plt.contourf(lons,lats,np.sqrt(uwnd300v00Z**2 + vwnd300v00Z**2)*1.94, bounds300, cmap=plt.cm.hot_r,transform=ccrs.PlateCarree())
plt.barbs(lons[::24,::24],lats[::24,::24],uwnd300v00Z[::24,::24],vwnd300v00Z[::24,::24],transform=ccrs.PlateCarree())

cbar=plt.colorbar(location='bottom')
cbar.set_label ('knots')

plt.title('31 Oct 00Z 300 mb Heights (dm) / Isotachs (knots)')

#End

#300MB 12Z Synoptic Map (Heights/Winds)

fig=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-120.,-70.,20.,50.])
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES, alpha=0.5)

gl=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False

gph30012Z=d12Z[117]
gph300v12Z=gph30012Z['values']

uwnd30012Z=d12Z[120]
uwnd300v12Z=uwnd30012Z['values']

vwnd30012Z=d12Z[121]
vwnd300v12Z=vwnd30012Z['values']

lats,lons=gph30012Z.latlons()

plt.contour(lons,lats,gph300v12Z,np.arange(8000,10000,100), linewidths=2, colors='black',transform=ccrs.PlateCarree())

bounds300=[30,40,60,80,100,125,150,175,200]
plt.contourf(lons,lats,np.sqrt(uwnd300v12Z**2 + vwnd300v12Z**2)*1.94, bounds300, cmap=plt.cm.hot_r,transform=ccrs.PlateCarree())
plt.barbs(lons[::24,::24],lats[::24,::24],uwnd300v12Z[::24,::24],vwnd300v12Z[::24,::24],transform=ccrs.PlateCarree())

cbar=plt.colorbar(location='bottom')
cbar.set_label ('knots')

plt.title('31 Oct 12Z 300 mb Heights (dm) / Isotachs (knots)')

#End

#500MB 00Z Synoptic Map (Heights/Winds/Vorticity)

fig=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-120.,-70.,20.,50.])
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES, alpha=0.5)

gl=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False

gph50000Z=d00Z[165]
gph500v00Z=gph50000Z['values']

uwnd50000Z=d00Z[168]
uwnd500v00Z=uwnd50000Z['values']

vwnd50000Z=d00Z[169]
vwnd500v00Z=vwnd50000Z['values']

av50000Z=d00Z[33]
av500v00Z=av50000Z['values']

lats,lons=gph50000Z.latlons()

boundsav=[18,24,30,36,42,48,54,60,66,72]

plt.contourf(lons,lats,av500v00Z*100000,boundsav,cmap=plt.cm.gist_ncar,transform=ccrs.PlateCarree())

cbar=plt.colorbar(location='bottom')
cbar.set_label ('10^-5 s^-1')

plt.contour(lons,lats,gph500v00Z,np.arange(4500,6500,80), linewidths=2, colors='black',transform=ccrs.PlateCarree())

plt.barbs(lons[::30,::30],lats[::30,::30],uwnd500v00Z[::30,::30],vwnd500v00Z[::30,::30],transform=ccrs.PlateCarree())

plt.title('31 Oct 00Z 500 mb Heights (dm) / Isotachs (kts) / Absolute Vorticity (10^-5)')

#End

#500MB 12Z Synoptic Map (Heights/Winds/Vorticity)

fig=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-120.,-70.,20.,50.])
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES, alpha=0.5)

gl=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False

gph50012Z=d12Z[165]
gph500v12Z=gph50012Z['values']

uwnd50012Z=d12Z[168]
uwnd500v12Z=uwnd50012Z['values']

vwnd50012Z=d00Z[169]
vwnd500v12Z=vwnd50012Z['values']

av50012Z=d12Z[33]
av500v12Z=av50012Z['values']

lats,lons=gph50012Z.latlons()

boundsav=[18,24,30,36,42,48,54,60,66,72]

plt.contourf(lons,lats,av500v12Z*100000,boundsav,cmap=plt.cm.gist_ncar,transform=ccrs.PlateCarree())

cbar=plt.colorbar(location='bottom')
cbar.set_label ('10^-5 s^-1')

plt.contour(lons,lats,gph500v12Z,np.arange(4500,6500,80), linewidths=2, colors='black',transform=ccrs.PlateCarree())

plt.barbs(lons[::30,::30],lats[::30,::30],uwnd500v12Z[::30,::30],vwnd500v12Z[::30,::30],transform=ccrs.PlateCarree())

plt.title('31 Oct 12Z 500 mb Heights (dm) / Isotachs (kts) / Absolute Vorticity (10^-5)')

#End

#850MB 00Z Synoptic Map (Heights/Winds/TEMP)

fig=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-120.,-70.,20.,50.])
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES, alpha=0.5)

gl=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False

gph85000Z=d00Z[249]
gph850v00Z=gph85000Z['values']

uwnd85000Z=d00Z[252]
uwnd850v00Z=uwnd85000Z['values']

vwnd85000Z=d00Z[253]
vwnd850v00Z=vwnd85000Z['values']

tmp85000Z=d00Z[250]
tmp850v00Z=tmp85000Z['values']

lats,lons=gph85000Z.latlons()

boundstmp=[-16,-12,-8,-4,00,4,8,12,16,20,24,28]

plt.contour(lons,lats,gph850v00Z,np.arange(1200,1600,30), linewidths=2, colors='black',transform=ccrs.PlateCarree())

plt.contourf(lons,lats,tmp850v00Z-273, boundstmp, cmap=plt.cm.RdBu_r,transform=ccrs.PlateCarree())

cbar=plt.colorbar(location='bottom')
cbar.set_label ('C')

plt.barbs(lons[::30,::30],lats[::30,::30],uwnd850v00Z[::30,::30],vwnd850v00Z[::30,::30],transform=ccrs.PlateCarree())

plt.title('31 Oct 00Z 850mb Heights (dm) / Temperature (C) / Isotachs (kts)')

#End

#850MB 12Z Synoptic Map (Heights/Winds/TEMP)

fig=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-120.,-70.,20.,50.])
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES, alpha=0.5)

gl=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False

gph85012Z=d12Z[249]
gph850v12Z=gph85012Z['values']

uwnd85012Z=d12Z[252]
uwnd850v12Z=uwnd85012Z['values']

vwnd85012Z=d12Z[253]
vwnd850v12Z=vwnd85012Z['values']

tmp85012Z=d12Z[250]
tmp850v12Z=tmp85012Z['values']

lats,lons=gph85012Z.latlons()

boundstmp=[-16,-12,-8,-4,00,4,8,12,16,20,24,28]

plt.contour(lons,lats,gph850v12Z,np.arange(1200,1600,30), linewidths=2, colors='black',transform=ccrs.PlateCarree())

plt.contourf(lons,lats,tmp850v12Z-273, boundstmp, cmap=plt.cm.RdBu_r,transform=ccrs.PlateCarree())

cbar=plt.colorbar(location='bottom')
cbar.set_label ('C')

plt.barbs(lons[::30,::30],lats[::30,::30],uwnd850v12Z[::30,::30],vwnd850v12Z[::30,::30],transform=ccrs.PlateCarree())

plt.title('31 Oct 12Z 850mb Heights (dm) / Temperature (C) / Isotachs (kts)')

#End

#SFC 00Z PWI Values

fig=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-120.,-70.,20.,50.])
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES, alpha=0.5)

gl=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False

pcpw00Z=d00Z[348]
pcpwv00Z=pcpw00Z['values']

lats,lons=pcpw00Z.latlons()

PWIbounds=[0,10,20,30,40,50,60,70,80]
plt.contourf(lons,lats,pcpwv00Z,PWIbounds,cmap=plt.cm.Greens,transform=ccrs.PlateCarree())

cbar=plt.colorbar(location='bottom')
cbar.set_label ('kg/m^2')

plt.title('31 Oct 00Z Precipitable Water (kg/m^2)')

#End

#SFC 12Z PWI Values

fig=plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-120.,-70.,20.,50.])
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES, alpha=0.5)

gl=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False

pcpw12Z=d12Z[348]
pcpwv12Z=pcpw12Z['values']

lats,lons=pcpw12Z.latlons()

PWIbounds=[0,10,20,30,40,50,60,70,80]
plt.contourf(lons,lats,pcpwv12Z,PWIbounds,cmap=plt.cm.Greens,transform=ccrs.PlateCarree())

cbar=plt.colorbar(location='bottom')
cbar.set_label ('kg/m^2')

plt.title('31 Oct 12Z Precipitable Water (kg/m^2)')

#End

def plot_bulletin(ax, data):
    """Plot a dataframe of surface features on a map."""
# Set some default visual styling
    size = 4
    fontsize = 9
    complete_style = {'HIGH': {'color': 'blue', 'fontsize': fontsize},
                      'LOW': {'color': 'red', 'fontsize': fontsize},
                      'WARM': {'linewidth': 1, 'path_effects': [WarmFront(size=size)]},
                      'COLD': {'linewidth': 1, 'path_effects': [ColdFront(size=size)]},
                      'OCFNT': {'linewidth': 1, 'path_effects': [OccludedFront(size=size)]},
                      'STNRY': {'linewidth': 1, 'path_effects': [StationaryFront(size=size)]},
                      'TROF': {'linewidth': 2, 'linestyle': 'dashed',
                               'edgecolor': 'darkorange'}}

# Handle H/L points using MetPy's StationPlot class
    for field in ('HIGH', 'LOW'):
        rows = data[data.feature == field]
        x, y = zip(*((pt.x, pt.y) for pt in rows.geometry))
        sp = StationPlot(ax, x, y, transform=ccrs.PlateCarree(), clip_on=True)
        sp.plot_text('C', [field[0]] * len(x), **complete_style[field])
        sp.plot_parameter('S', rows.strength, **complete_style[field])

# Handle all the boundary types
    for field in ('WARM', 'COLD', 'STNRY', 'OCFNT', 'TROF'):
        rows = data[data.feature == field]
        ax.add_geometries(rows.geometry, crs=ccrs.PlateCarree(), **complete_style[field],
                          facecolor='none')

# Set up a default figure and map
fig = plt.figure(figsize=(8, 8), dpi=150)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.LambertConformal(central_longitude=-100))
ax.set_extent([235,290,20,55])
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.LAND)
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.STATES)
ax.add_feature(cf.LAKES)


# Parse the bulletin and plot it
df = parse_wpc_surface_bulletin('CODSUS_201310310000_00Z.txt')
plot_bulletin(ax, df)

ax.set_title(f'WPC Surface Analysis Valid {df.valid.dt.strftime("%HZ %d %b %Y")[0]}')

plt.show()

#End

#31 Oct 12Z

def plot_bulletin(ax, data):
    """Plot a dataframe of surface features on a map."""
# Set some default visual styling
    size = 4
    fontsize = 9
    complete_style = {'HIGH': {'color': 'blue', 'fontsize': fontsize},
                      'LOW': {'color': 'red', 'fontsize': fontsize},
                      'WARM': {'linewidth': 1, 'path_effects': [WarmFront(size=size)]},
                      'COLD': {'linewidth': 1, 'path_effects': [ColdFront(size=size)]},
                      'OCFNT': {'linewidth': 1, 'path_effects': [OccludedFront(size=size)]},
                      'STNRY': {'linewidth': 1, 'path_effects': [StationaryFront(size=size)]},
                      'TROF': {'linewidth': 2, 'linestyle': 'dashed',
                               'edgecolor': 'darkorange'}}

# Handle H/L points using MetPy's StationPlot class
    for field in ('HIGH', 'LOW'):
        rows = data[data.feature == field]
        x, y = zip(*((pt.x, pt.y) for pt in rows.geometry))
        sp = StationPlot(ax, x, y, transform=ccrs.PlateCarree(), clip_on=True)
        sp.plot_text('C', [field[0]] * len(x), **complete_style[field])
        sp.plot_parameter('S', rows.strength, **complete_style[field])

# Handle all the boundary types
    for field in ('WARM', 'COLD', 'STNRY', 'OCFNT', 'TROF'):
        rows = data[data.feature == field]
        ax.add_geometries(rows.geometry, crs=ccrs.PlateCarree(), **complete_style[field],
                          facecolor='none')

# Set up a default figure and map
fig = plt.figure(figsize=(8, 8), dpi=150)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.LambertConformal(central_longitude=-100))
ax.set_extent([235,290,20,55])
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.LAND)
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.STATES)
ax.add_feature(cf.LAKES)


# Parse the bulletin and plot it
df = parse_wpc_surface_bulletin('CODSUS_201310311330_12Z.txt')
plot_bulletin(ax, df)

ax.set_title(f'WPC Surface Analysis Valid {df.valid.dt.strftime("%HZ %d %b %Y")[0]}')

#End


#Importing matplotlib and csv in order to read csv files and plot their data.
import matplotlib.pyplot as plt
import csv

#Scatterplot for Austin Bergstrom-------------------

#Reading the Data in teh csv file format:
data=[]
with open('AustinBergstrom_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
#Setting up variables for refrence when plotting the correct data on the graphs:
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

#Using matplotlib to plot the data:
plt.plot(p01i, valid, 'co')

#Ploting the x data with title:
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')

#Rotating x-labels 45 degrees to make plots easier to read and fix oversaturation of values:
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)

#Plotting the y data with title:
plt.ylabel('Precipitation Fallen in 1 hr (in)')

#Creating Title for the Graph and creating a gridded plot with x and y data:
plt.title('1 hr Precipitation for Austin Bergstrom Int. Airport, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Same process is repeated for all other plots:

#Scatterplot for Austin Camp Mabry------------------
data=[]
with open('AustinCampMabry_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Austin Camp Mabry, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for Austin EDC------------------------
data=[]
with open('AustinEDC_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Austin City METAR, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for Georgetown----------------------
data=[]
with open('Georgetown_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Georgetown, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for Giddings------------------------
data=[]
with open('Giddings_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Giddings, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for Horseshoe-----------------------
data=[]
with open('Horseshoe_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Horseshoe, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for Lago Vista----------------------
data=[]
with open('LagoVista_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Lago Vista, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for New Braunfels------------------
data=[]
with open('NewBraunfels_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for New Braunfels, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for San Marcos---------------------
data=[]
with open('SanMarcos_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for San Marcos, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#End

crl=open('coloradoriverlevels.txt')

crllines=crl.readlines()

rl=[]
time=[]
date=[]

for i in range(125,221):
    crldata=crllines[i]
    data=crldata.split()
    for index in range(len(data)):
        columns = crldata.split()
        rainfall=columns[5]
        times=columns[3]
        dates=columns[2]
        rl.append(float(rainfall))
        time.append(times)
        date.append(dates)
newtime=[item.replace(':','') for item in time]
plt.plot(time, rl,color='g')
plt.ylabel("Water Level (ft)")
plt.xlabel("Time (CDT)")
plt.xticks(time[::70],rotation=45)
plt.grid(True)
plt.title("Colorado River at Austin, TX October 31,2013")

#End

walcl=open('walnutcreeklevels103113.txt')

walcllines=walcl.readlines()

rl=[]
time=[]
date=[]

for i in range(316,603):
    walcldata=walcllines[i]
    data=walcldata.split()
    for index in range(len(data)):
        columns = walcldata.split()
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
plt.title("Walnut Ck at Webberville Rd, Austin, TX October 31, 2013 ")

#End

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

#End

f = Level2File('KEWX20131031_180016_V06 (1)')

print(f.sweeps[0][0])
###########################################

# Pull data out of the file
sweep = 0

# First item in ray is header, which has azimuth angle
az = np.array([ray[0].az_angle for ray in f.sweeps[sweep]])

###########################################
# We need to take the single azimuth (nominally a mid-point) we get in the data and
# convert it to be the azimuth of the boundary between rays of data, taking care to handle
# where the azimuth crosses from 0 to 360.
diff = np.diff(az)
crossed = diff < -180
diff[crossed] += 360.
avg_spacing = diff.mean()

# Convert mid-point to edge
az = (az[:-1] + az[1:]) / 2
az[crossed] += 180.

# Concatenate with overall start and end of data we calculate using the average spacing
az = np.concatenate(([az[0] - avg_spacing], az, [az[-1] + avg_spacing]))
az = units.Quantity(az, 'degrees')

###########################################
# Calculate ranges for the gates from the metadata

# 5th item is a dict mapping a var name (byte string) to a tuple
# of (header, data array)
ref_hdr = f.sweeps[sweep][0][4][b'REF'][0]
ref_range = (np.arange(ref_hdr.num_gates + 1) - 0.5) * ref_hdr.gate_width + ref_hdr.first_gate
ref_range = units.Quantity(ref_range, 'kilometers')
ref = np.array([ray[4][b'REF'][1] for ray in f.sweeps[sweep]])

rho_hdr = f.sweeps[sweep][0][4][b'RHO'][0]
rho_range = (np.arange(rho_hdr.num_gates + 1) - 0.5) * rho_hdr.gate_width + rho_hdr.first_gate
rho_range = units.Quantity(rho_range, 'kilometers')
rho = np.array([ray[4][b'RHO'][1] for ray in f.sweeps[sweep]])

# Extract central longitude and latitude from file
cent_lon = f.sweeps[0][0][1].lon
cent_lat = f.sweeps[0][0][1].lat
###########################################
#spec=gridspec.GridSpec(1, 2)
spec = gridspec.GridSpec(1, 1)
#fig = plt.figure(figsize=(15, 8))
fig = plt.figure(figsize=(8,8))

for var_data, var_range, ax_rect in zip((ref, rho), (ref_range, rho_range), spec):
    # Turn into an array, then mask
    data = np.ma.array(var_data)
    data[np.isnan(data)] = np.ma.masked

    # Convert az,range to x,y
    xlocs, ylocs = azimuth_range_to_lat_lon(az, var_range, cent_lon, cent_lat)

    # Plot the data
    crs = ccrs.LambertConformal(central_longitude=cent_lon, central_latitude=cent_lat)
    ax = fig.add_subplot(ax_rect, projection=crs)
    ax.add_feature(USCOUNTIES, linewidth=0.5)
    ax.pcolormesh(xlocs, ylocs, data, cmap='Spectral_r', transform=ccrs.PlateCarree())
    ax.set_extent([cent_lon - 3, cent_lon + 3, cent_lat - 3, cent_lat + 3])
    ax.set_aspect('equal', 'datalim')
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=2, color='grey', alpha=0.5, linestyle='--')
    plt.title("KEWX - AUSTIN/S ANT, TX Radar 6:00 PM CDT Oct. 31")
    #add_timestamp(ax, f.dt, y=0.02, high_contrast=True)

plt.show()

#End

###########################################
# Open the file

f = Level2File('KEWX20131031_120325_V06')

print(f.sweeps[0][0])
###########################################

# Pull data out of the file
sweep = 0

# First item in ray is header, which has azimuth angle
az = np.array([ray[0].az_angle for ray in f.sweeps[sweep]])

###########################################
# We need to take the single azimuth (nominally a mid-point) we get in the data and
# convert it to be the azimuth of the boundary between rays of data, taking care to handle
# where the azimuth crosses from 0 to 360.
diff = np.diff(az)
crossed = diff < -180
diff[crossed] += 360.
avg_spacing = diff.mean()

# Convert mid-point to edge
az = (az[:-1] + az[1:]) / 2
az[crossed] += 180.

# Concatenate with overall start and end of data we calculate using the average spacing
az = np.concatenate(([az[0] - avg_spacing], az, [az[-1] + avg_spacing]))
az = units.Quantity(az, 'degrees')

###########################################
# Calculate ranges for the gates from the metadata

# 5th item is a dict mapping a var name (byte string) to a tuple
# of (header, data array)
ref_hdr = f.sweeps[sweep][0][4][b'REF'][0]
ref_range = (np.arange(ref_hdr.num_gates + 1) - 0.5) * ref_hdr.gate_width + ref_hdr.first_gate
ref_range = units.Quantity(ref_range, 'kilometers')
ref = np.array([ray[4][b'REF'][1] for ray in f.sweeps[sweep]])

rho_hdr = f.sweeps[sweep][0][4][b'RHO'][0]
rho_range = (np.arange(rho_hdr.num_gates + 1) - 0.5) * rho_hdr.gate_width + rho_hdr.first_gate
rho_range = units.Quantity(rho_range, 'kilometers')
rho = np.array([ray[4][b'RHO'][1] for ray in f.sweeps[sweep]])

# Extract central longitude and latitude from file
cent_lon = f.sweeps[0][0][1].lon
cent_lat = f.sweeps[0][0][1].lat
###########################################
#spec=gridspec.GridSpec(1, 2)
spec = gridspec.GridSpec(1, 1)
#fig = plt.figure(figsize=(15, 8))
fig = plt.figure(figsize=(8,8))

for var_data, var_range, ax_rect in zip((ref, rho), (ref_range, rho_range), spec):
    # Turn into an array, then mask
    data = np.ma.array(var_data)
    data[np.isnan(data)] = np.ma.masked

    # Convert az,range to x,y
    xlocs, ylocs = azimuth_range_to_lat_lon(az, var_range, cent_lon, cent_lat)

    # Plot the data
    crs = ccrs.LambertConformal(central_longitude=cent_lon, central_latitude=cent_lat)
    ax = fig.add_subplot(ax_rect, projection=crs)
    ax.add_feature(USCOUNTIES, linewidth=0.5)
    ax.pcolormesh(xlocs, ylocs, data, cmap='Spectral_r', transform=ccrs.PlateCarree())
    ax.set_extent([cent_lon - 3, cent_lon + 3, cent_lat - 3, cent_lat + 3])
    ax.set_aspect('equal', 'datalim')
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=2, color='grey', alpha=0.5, linestyle='--')
    plt.title("KEWX - AUSTIN/S ANT, TX Radar 12:03 PM CDT Oct. 31")
    #add_timestamp(ax, f.dt, y=0.02, high_contrast=True)

plt.show()

#End

###########################################
# Open the file

f = Level2File('KEWX20131031_000403_V06')

print(f.sweeps[0][0])
###########################################

# Pull data out of the file
sweep = 0

# First item in ray is header, which has azimuth angle
az = np.array([ray[0].az_angle for ray in f.sweeps[sweep]])

###########################################
# We need to take the single azimuth (nominally a mid-point) we get in the data and
# convert it to be the azimuth of the boundary between rays of data, taking care to handle
# where the azimuth crosses from 0 to 360.
diff = np.diff(az)
crossed = diff < -180
diff[crossed] += 360.
avg_spacing = diff.mean()

# Convert mid-point to edge
az = (az[:-1] + az[1:]) / 2
az[crossed] += 180.

# Concatenate with overall start and end of data we calculate using the average spacing
az = np.concatenate(([az[0] - avg_spacing], az, [az[-1] + avg_spacing]))
az = units.Quantity(az, 'degrees')

###########################################
# Calculate ranges for the gates from the metadata

# 5th item is a dict mapping a var name (byte string) to a tuple
# of (header, data array)
ref_hdr = f.sweeps[sweep][0][4][b'REF'][0]
ref_range = (np.arange(ref_hdr.num_gates + 1) - 0.5) * ref_hdr.gate_width + ref_hdr.first_gate
ref_range = units.Quantity(ref_range, 'kilometers')
ref = np.array([ray[4][b'REF'][1] for ray in f.sweeps[sweep]])

rho_hdr = f.sweeps[sweep][0][4][b'RHO'][0]
rho_range = (np.arange(rho_hdr.num_gates + 1) - 0.5) * rho_hdr.gate_width + rho_hdr.first_gate
rho_range = units.Quantity(rho_range, 'kilometers')
rho = np.array([ray[4][b'RHO'][1] for ray in f.sweeps[sweep]])

# Extract central longitude and latitude from file
cent_lon = f.sweeps[0][0][1].lon
cent_lat = f.sweeps[0][0][1].lat
###########################################
#spec=gridspec.GridSpec(1, 2)
spec = gridspec.GridSpec(1, 1)
#fig = plt.figure(figsize=(15, 8))
fig = plt.figure(figsize=(8,8))

for var_data, var_range, ax_rect in zip((ref, rho), (ref_range, rho_range), spec):
    # Turn into an array, then mask
    data = np.ma.array(var_data)
    data[np.isnan(data)] = np.ma.masked

    # Convert az,range to x,y
    xlocs, ylocs = azimuth_range_to_lat_lon(az, var_range, cent_lon, cent_lat)

    # Plot the data
    crs = ccrs.LambertConformal(central_longitude=cent_lon, central_latitude=cent_lat)
    ax = fig.add_subplot(ax_rect, projection=crs)
    ax.add_feature(USCOUNTIES, linewidth=0.5)
    ax.pcolormesh(xlocs, ylocs, data, cmap='Spectral_r', transform=ccrs.PlateCarree())
    ax.set_extent([cent_lon - 3, cent_lon + 3, cent_lat - 3, cent_lat + 3])
    ax.set_aspect('equal', 'datalim')
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=2, color='grey', alpha=0.5, linestyle='--')
    plt.title("KEWX - AUSTIN/S ANT, TX Radar 12:04 AM CDT Oct. 31")
    #add_timestamp(ax, f.dt, y=0.02, high_contrast=True)

plt.show()

#End

###########################################
# Open the file

f = Level2File('KEWX20131031_060235_V06')

print(f.sweeps[0][0])
###########################################

# Pull data out of the file
sweep = 0

# First item in ray is header, which has azimuth angle
az = np.array([ray[0].az_angle for ray in f.sweeps[sweep]])

###########################################
# We need to take the single azimuth (nominally a mid-point) we get in the data and
# convert it to be the azimuth of the boundary between rays of data, taking care to handle
# where the azimuth crosses from 0 to 360.
diff = np.diff(az)
crossed = diff < -180
diff[crossed] += 360.
avg_spacing = diff.mean()

# Convert mid-point to edge
az = (az[:-1] + az[1:]) / 2
az[crossed] += 180.

# Concatenate with overall start and end of data we calculate using the average spacing
az = np.concatenate(([az[0] - avg_spacing], az, [az[-1] + avg_spacing]))
az = units.Quantity(az, 'degrees')

###########################################
# Calculate ranges for the gates from the metadata

# 5th item is a dict mapping a var name (byte string) to a tuple
# of (header, data array)
ref_hdr = f.sweeps[sweep][0][4][b'REF'][0]
ref_range = (np.arange(ref_hdr.num_gates + 1) - 0.5) * ref_hdr.gate_width + ref_hdr.first_gate
ref_range = units.Quantity(ref_range, 'kilometers')
ref = np.array([ray[4][b'REF'][1] for ray in f.sweeps[sweep]])

rho_hdr = f.sweeps[sweep][0][4][b'RHO'][0]
rho_range = (np.arange(rho_hdr.num_gates + 1) - 0.5) * rho_hdr.gate_width + rho_hdr.first_gate
rho_range = units.Quantity(rho_range, 'kilometers')
rho = np.array([ray[4][b'RHO'][1] for ray in f.sweeps[sweep]])

# Extract central longitude and latitude from file
cent_lon = f.sweeps[0][0][1].lon
cent_lat = f.sweeps[0][0][1].lat
###########################################
#spec=gridspec.GridSpec(1, 2)
spec = gridspec.GridSpec(1, 1)
#fig = plt.figure(figsize=(15, 8))
fig = plt.figure(figsize=(8,8))

for var_data, var_range, ax_rect in zip((ref, rho), (ref_range, rho_range), spec):
    # Turn into an array, then mask
    data = np.ma.array(var_data)
    data[np.isnan(data)] = np.ma.masked

    # Convert az,range to x,y
    xlocs, ylocs = azimuth_range_to_lat_lon(az, var_range, cent_lon, cent_lat)

    # Plot the data
    crs = ccrs.LambertConformal(central_longitude=cent_lon, central_latitude=cent_lat)
    ax = fig.add_subplot(ax_rect, projection=crs)
    ax.add_feature(USCOUNTIES, linewidth=0.5)
    ax.pcolormesh(xlocs, ylocs, data, cmap='Spectral_r', transform=ccrs.PlateCarree())
    ax.set_extent([cent_lon - 3, cent_lon + 3, cent_lat - 3, cent_lat + 3])
    ax.set_aspect('equal', 'datalim')
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=2, color='grey', alpha=0.5, linestyle='--')
    plt.title("KEWX - AUSTIN/S ANT, TX Radar 6:02 AM CDT Oct. 31")
    #add_timestamp(ax, f.dt, y=0.02, high_contrast=True)

plt.show()

#End

plt.show()
d12Z.close()
d00Z.close()
f.close()