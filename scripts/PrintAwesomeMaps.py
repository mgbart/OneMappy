# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:03:16 2022

@author: matia
"""

import matplotlib.pyplot as plt
import math

import csv

from MapPlot import plot, setStyle


# Global Variables

# Earth’s radius, sphere
R=6378137



with open("../import.csv") as csvFile:   #open the file
  CSVdata = csv.reader(csvFile, delimiter=',')  #read the data
  header = next(CSVdata) # To skip header with column names in FOR loop
  
  for row in CSVdata:   #loop through each row
    location, lat, lon, dist, style = row
    print(row)   #print the data
    
    lat = float(lat)
    lon = float(lon)
    dist = float(dist)
    
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
    file_parks = "../out/" + location + "_" + style + "_3_parks.png"
    file_greens = "../out/" + location + "_" + style + "_2_green_areas.png"
    file_water = "../out/" + location + "_" + style + "_1_water.png"



    color_motorways, color_primary, color_residential, color_parks, color_greens, color_water = setStyle(style=style)
    
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
         file_water=file_water
         )


