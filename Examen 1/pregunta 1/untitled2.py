# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:37:02 2024

@author: RODO
"""

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir los nodos
G.add_node("Abraham Simpson")
G.add_node("Mona Simpson")
G.add_node("Homer Simpson")
G.add_node("Marge Simpson")
G.add_node("Bart Simpson")
G.add_node("Lisa Simpson")
G.add_node("Maggie Simpson")
G.add_node("Patty Bouvier")
G.add_node("Selma Bouvier")

# Añadir las aristas que representan las relaciones familiares
G.add_edge("Abraham Simpson", "Homer Simpson")
G.add_edge("Mona Simpson", "Homer Simpson")
G.add_edge("Homer Simpson", "Bart Simpson")
G.add_edge("Homer Simpson", "Lisa Simpson")
G.add_edge("Homer Simpson", "Maggie Simpson")
G.add_edge("Marge Simpson", "Bart Simpson")
G.add_edge("Marge Simpson", "Lisa Simpson")
G.add_edge("Marge Simpson", "Maggie Simpson")
G.add_edge("Patty Bouvier", "Marge Simpson")
G.add_edge("Selma Bouvier", "Marge Simpson")

# Dibujar el grafo con una disposición de árbol y nodos más grandes
pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='dot')
plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, arrows=False, node_size=15000)
plt.show()

