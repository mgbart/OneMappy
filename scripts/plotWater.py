# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:42:31 2022

@author: matia
"""

import osmnx as ox
import geopandas as gpd




def plotWater(bN, bE, bS, bW, lat, lon, dist, water_color, fileName):
    
    outFile1 = "../out/" + fileName + "_water.png"
    
    # Fetch water
    G = ox.geometries.geometries_from_bbox(bN, bS, bE, bW, tags={"natural": "water"})
    # Load coastline polygons
    water = gpd.read_file('../assets/water-polygons-split-4326/water_polygons.shp', bbox=(bW, bN, bE, bS))
    # Plot
    fig, ax = ox.plot_footprints(water, bbox=(bN, bS, bE, bW), figsize=(27, 40), 
                            dpi = 300,
                            color=water_color, 
                            show=False, close=False)
    ax = G.plot(ax=ax, fc=water_color, markersize=0)
    
    fig.tight_layout(pad=0)
    fig.savefig(outFile1, dpi=300, bbox_inches='tight', format="png", facecolor=fig.get_facecolor(), transparent=True)
    
