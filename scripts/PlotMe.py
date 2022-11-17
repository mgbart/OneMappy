# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 23:24:50 2022

@author: Matias Bernhardt
"""


import math
import csv
import argparse

from MapPlot import plot, setStyle, setPrintSize


# Global Variables

# Earth’s radius, sphere
R=6378137



parser = argparse.ArgumentParser("MapPlotBot")
parser.add_argument("location", help="Name of location. The name will be the prefix on the output files.", type=str)
parser.add_argument("lat", help="Latitude for map center", type=float)
parser.add_argument("lon", help="Longitude for map center", type=float)
parser.add_argument("dist", help="Distance from map center in meters", type=float)
parser.add_argument("style", help="Predefined syle template. Refer for wiki for a list of available styles.", type=str)
parser.add_argument("papersize", help="Size of output in DIN format", type=str)
parser.add_argument("dpi", help="Output DPI.", type=float)
args = parser.parse_args()

location = args.location
lat = args.lat
lon = args.lon
dist = args.dist
style = args.style
paperSize = args.papersize
dpi = args.dpi


    
point = (lat, lon)# offsets in meters
dn = dist
de = dist
# Coordinate offsets in radians
dLat = dn/R
dLon = de/(R*(math.cos((math.pi)*lat/180)))


bN = lat + dLat * 180/(math.pi)
bE = lon + dLon * 180/(math.pi)
bS = lat - dLat * 180/(math.pi) 
bW = lon - dLon * 180/(math.pi)



# File Names
file_motorways = "../out/" + location + "_" + style + "_6_motorway_trunk.png"
file_primary = "../out/" + location + "_" + style + "_5_primary_secondary.png"
file_residential = "../out/" + location + "_" + style + "_4_residential.png"
file_water = "../out/" + location + "_" + style + "_3_water.png"
file_parks = "../out/" + location + "_" + style + "_2_parks.png"
file_greens = "../out/" + location + "_" + style + "_1_green_areas.png"



color_motorways, color_primary, color_residential, color_parks, color_greens, color_water = setStyle(style=style)

width, height = setPrintSize(paperSize) 

plot(point=point,
     dist=dist,
     bN=bN,
     bS=bS,
     bE=bE,
     bW=bW,
     color_motorways=color_motorways,
     color_primary=color_primary,
     color_residential=color_residential,
     color_parks=color_parks,
     color_greens=color_greens,
     color_water=color_water,
     file_motorways=file_motorways,
     file_primary=file_primary,
     file_residential=file_residential,
     file_parks=file_parks,
     file_greens=file_greens,
     file_water=file_water,
     width=width,
     height=height,
     dpi=dpi
     )


