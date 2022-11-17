# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 16:20:29 2022

@author: Matias Bernhardt
"""
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt







def plot(point, dist, bN, bS, bE, bW, color_motorways, color_primary, color_residential, color_parks, color_greens, color_water, file_motorways, file_primary, file_residential, file_parks, file_greens, file_water, width, height, dpi):

    G = ox.graph_from_point(point, dist=dist, custom_filter=('["highway"~"motorway|trunk"]'), simplify=True, truncate_by_edge=True, retain_all = True )
    
    fig, ax = ox.plot_graph(G, bbox=(bN, bS, bE, bW) ,
                            node_size=0,
                            figsize=(width, height),
                            dpi = dpi,
                            edge_color=color_motorways,
                            edge_linewidth=2,
                            edge_alpha=1)
    
    fig.tight_layout(pad=0)
    fig.savefig(file_motorways,  dpi=dpi, bbox_inches='tight', pad_inches=0, format="png", facecolor=fig.get_facecolor(), transparent=True)
    
    
    
    G = ox.graph_from_point(point, dist=dist, custom_filter=('["highway"~"primary|secondary"]'), simplify=True, truncate_by_edge=True, retain_all = True )
    
    fig, ax = ox.plot_graph(G, bbox=(bN, bS, bE, bW), 
                            node_size=0,
                            figsize=(width, height),
                            dpi = dpi,
                            edge_color=color_primary,
                            edge_linewidth=1,
                             edge_alpha=1)
    fig.tight_layout(pad=0)
    fig.savefig(file_primary, dpi=dpi, bbox_inches='tight', pad_inches=0, format="png", facecolor=fig.get_facecolor(), transparent=True)
    
    
    
    
    
    G = ox.graph_from_point(point, dist=dist, custom_filter=('["highway"~"residential|tertiary"]'), simplify=True, truncate_by_edge=True, retain_all = True )
    
    fig, ax = ox.plot_graph(G, bbox=(bN, bS, bE, bW), 
                            node_size=0,
                            figsize=(width, height),
                            dpi = dpi,
                            edge_color=color_residential,
                            edge_linewidth=0.75,
                            edge_alpha=1)
    fig.tight_layout(pad=0)
    fig.savefig(file_residential, dpi=dpi, bbox_inches='tight', pad_inches=0, format="png", facecolor=fig.get_facecolor(), transparent=True)
    
    
    
    leisure = ox.geometries_from_bbox(bN, bS, bE, bW, tags={'leisure':True})
    
    parks = leisure[leisure["leisure"].isin(["pitch","park","playground", "cemetery"])]
    # Plot
    fig, ax = ox.plot_footprints(parks, bbox=(bN, bS, bE, bW), 
                            figsize=(width, height),
                            dpi = dpi,
                            color=color_parks, 
                            show=False, close=False)
    ax = parks.plot(ax=ax, fc=color_parks, markersize=0)
    fig.tight_layout(pad=0)
    fig.savefig(file_parks, dpi=dpi, bbox_inches='tight', pad_inches=0, format="png", facecolor=fig.get_facecolor(), transparent=True)
    
    
    landuse = ox.geometries_from_bbox(bN, bS, bE, bW, tags={'landuse':True})
    greens = landuse[landuse["landuse"].isin(["forest","farmland","farmyard", "meadow", "orchard", "vineyard"])]
    # Plot
    fig, ax = ox.plot_footprints(greens, bbox=(bN, bS, bE, bW),
                            figsize=(width, height),
                            dpi = dpi,
                            color=color_greens, 
                            show=False, close=False)
    ax = greens.plot(ax=ax, fc=color_greens, markersize=0)
    fig.tight_layout(pad=0)
    fig.savefig(file_greens, dpi=dpi, bbox_inches='tight', pad_inches=0, format="png", facecolor=fig.get_facecolor(), transparent=True)
    
    
    
    # Fetch water
    G = ox.geometries.geometries_from_bbox(bN, bS, bE, bW, tags={"natural": "water"})
    # Load coastline polygons
    water = gpd.read_file('../assets/water-polygons-split-4326/water_polygons.shp', bbox=(bW, bN, bE, bS))
    # Plot
    fig, ax = ox.plot_footprints(water, bbox=(bN, bS, bE, bW),
                            figsize=(width, height),
                            dpi = dpi,
                            color=color_water, 
                            show=False, close=False)
    ax = G.plot(ax=ax, fc=color_water, markersize=0)
    
    fig.tight_layout(pad=0)
    fig.savefig(file_water, dpi=dpi, bbox_inches='tight', pad_inches=0, format="png", facecolor=fig.get_facecolor(), transparent=True)
    
def setPrintSize(paperSize):
    if paperSize == "A3":
        width = 11.7
        height = 16.5
        
    elif paperSize == "A4":
        width = 8.3
        height = 11.7
     
    else:
        width = 8.3
        height = 11.7

    
    return width, height
    
     
    
def setStyle(style):

    if style == "green-rivers":    
        color_motorways = "#D9D9D9" 
        color_primary = "#D9D9D9"
        color_residential = "#D9D9D9"
        color_parks = "#8C8C8C"
        color_greens = "#8C8C8C"
        color_water = "#275950"
        
    elif style == "orange":    
        color_motorways = "#F2ECCE" 
        color_primary = "#F2ECCE"
        color_residential = "#F2ECCE"
        color_parks = "#6CA663"
        color_greens = "#a5be59"
        color_water = "#F2ECCE"
        # BG Color for illustrator: #F2A413 or #F2BB16
        
    elif style == "black-on-white":    
        color_motorways = "#26211d" 
        color_primary = "#26211d"
        color_residential = "#26211d"
        color_parks = "#26211d"
        color_greens = "#26211d"
        color_water = "#499ec7"
        # BG Color for illustrator: #F2A413 or #F2BB16
        
    elif style == "natural":    
        color_motorways = "#f1f2ea" 
        color_primary = "#f1f2ea"
        color_residential = "#f1f2ea"
        color_parks = "#a5be59"
        color_greens = "#657c46"
        color_water = "#99bcbe"
        # BG Color for illustrator: #a5977d
        
    elif style == "high-contrast":    
        color_motorways = "#ffffff" 
        color_primary = "#ffffff"
        color_residential = "#ffffff"
        color_parks = "#a5be59"
        color_greens = "#657c46"
        color_water = "#000000"
        # BG Color for illustrator: #
        
    elif style == "laser-flat":    
        color_motorways = "#000000" 
        color_primary = "#000000"
        color_residential = "#000000"
        color_parks = "#00ff00"
        color_greens = "#00cc00"
        color_water = "#ffffff"
        # BG Color for illustrator: #ffffff
        
    elif style == "treasure-map":    
        color_motorways = "#c64c53" 
        color_primary = "#c64c53"
        color_residential = "#c64c53"
        color_parks = "#b9d7ab"
        color_greens = "#b9d7ab"
        color_water = "#7dc1a8"
        # BG Color for illustrator: #f5ead0
        
    elif style == "night":    
        color_motorways = "#f8ee98" 
        color_primary = "#f8ee98"
        color_residential = "#f8ee98"
        color_parks = "#060705"
        color_greens = "#060705"
        color_water = "#010307"
        # BG Color for illustrator: #ffffff
        
    
        
    #elif style == "tuev":    
    #    color_motorways = "#f7e8c7" 
    #    color_primary = "#f7e8c7"
    #    color_residential = "#f7e8c7"
    #    color_parks = "#353432"
    #    color_greens = "#353432"
    #    color_water = "#0a71b9"
        # BG Color for illustrator: #F2A413 or #F2BB16
    
    elif style == "tuev":    
        color_motorways = "#000000" 
        color_primary = "#000000"
        color_residential = "#000000"
        color_parks = "#ffffff"
        color_greens = "#ffffff"
        color_water = "#0a71b9"
        # BG Color for illustrator: #F2A413 or #F2BB16
        
    else:   
        color_motorways = "#f5f0dc" 
        color_primary = "#f5f0dc"
        color_residential = "#f5f0dc"
        color_parks = "#040001"
        color_greens = "#040001"
        color_water = "#f5f0dc"
        # BG Color for illustrator: #040001
        
    return color_motorways, color_primary, color_residential, color_parks, color_greens, color_water