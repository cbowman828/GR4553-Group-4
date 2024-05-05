# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:56:04 2024

@author: buske
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.feature as cf
import cartopy.crs as ccrs
import pygrib
from metpy.io import parse_wpc_surface_bulletin
from metpy.plots import (ColdFront, OccludedFront, StationaryFront, StationPlot, WarmFront)

f=open('Group4Project.txt','w')

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





plt.show()
d12Z.close()
d00Z.close()
f.close()















