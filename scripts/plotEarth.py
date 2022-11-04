# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 21:24:30 2022

@author: Matias Bernhardt
"""

import osmnx as ox

#point = (41.4266361, -73.6788272)

def plotEarth(lat, lon, dist, bN, bS, bE, bW, land_color, fileName):
    
    outFile = "../out/" + fileName + "_roads.png"
    
    point = (lat, lon)


    G = ox.graph_from_point(point, dist=dist, retain_all=True, simplify = True, network_type='all')
    
    u = []
    v = []
    key = []
    data = []
    for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
        u.append(uu)
        v.append(vv)
        key.append(kkey)
        data.append(ddata)    
    
    # List to store colors
    roadColors = []
    roadWidths = []
    
    
    for item in data:
        if "length" in item.keys():
            if item["length"] <= 100:
                linewidth = 1.0
                color = "#111111" 
                
            elif item["length"] > 100 and item["length"] <= 200:
                linewidth = 1.5
                color = "#111111"
                
            elif item["length"] > 200 and item["length"] <= 400:
                linewidth = 2.5
                color = "#111111"
                
            elif item["length"] > 400 and item["length"] <= 800:
                color = "#111111"
                linewidth = 3.5
            else:
                color = "#111111"
                linewidth = 4.5
        else:
            color = "#111111"
            linewidth = 1.0
            
        roadWidths.append(linewidth)
                
        roadColors.append(color)
        roadWidths.append(linewidth)
    '''
    
    for item in data:
        if "length" in item.keys():
            if item["length"] <= 100:
                linewidth = 0.10
                color = "#a6a6a6" 
                
            elif item["length"] > 100 and item["length"] <= 200:
                linewidth = 0.15
                color = "#676767"
                
            elif item["length"] > 200 and item["length"] <= 400:
                linewidth = 0.25
                color = "#454545"
                
            elif item["length"] > 400 and item["length"] <= 800:
                color = "#d5d5d5"
                linewidth = 0.35
            else:
                color = "#ededed"
                linewidth = 0.45
        else:
            color = "#a6a6a6"
            linewidth = 0.10
                
        roadColors.append(color)
        roadWidths.append(linewidth)
    
    '''
    
    bgcolor = land_color
    
    fig, ax = ox.plot_graph(G, bbox=(bN, bS, bE, bW), node_size=0,figsize=(27, 40), 
                            dpi = 300,
                            save = False, edge_color=roadColors,
                            edge_linewidth=roadWidths, edge_alpha=1)
    

    
    
    fig.tight_layout(pad=0)
    fig.savefig(outFile, dpi=300, bbox_inches='tight', format="png", facecolor=fig.get_facecolor(), transparent=True)