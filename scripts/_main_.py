# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 21:50:23 2022

@author: matia
"""

from plotEarth import plotEarth
from plotWater import plotWater
import math

name = "Manhattan"
lat, lon = 40.73716042794254, -73.96679483402386
dist = 6200

land_color = "#E9E5E4"
#water_color = '#93C2B2'

water_color = '#00A897'


# Earth’s radius, sphere
R=6378137

# offsets in meters
dn = dist
de = dist

# Coordinate offsets in radians
dLat = dn/R
dLon = de/(R*(math.cos((math.pi)*lat/180)))

# OffsetPosition, decimal degrees
bN = lat + dLat * 180/(math.pi)
bE = lon + dLon * 180/(math.pi)
bS = lat - dLat * 180/(math.pi)
bW = lon - dLon * 180/(math.pi)




plotEarth(lat, lon, dist, bN, bS, bE, bW, land_color, fileName=name)

plotWater(bN, bE, bS, bW, lat, lon, dist, water_color, fileName=name)