# -*- coding: utf-8 -*-
"""
Created on Wed May 15 00:41:43 2024

@author: RODO
"""

import numpy as np

# Coordenadas de los vértices de un cubo en 3D
cube = np.array([[-1, -1, -1],
                 [1, -1, -1],
                 [-1, 1, -1],
                 [1, 1, -1],
                 [-1, -1, 1],
                 [1, -1, 1],
                 [-1, 1, 1],
                 [1, 1, 1]])

# Coordenadas de los vértices de un dodecaedro
dodecahedron = np.vstack([cube, cube/np.sqrt(3), cube.T]).T

# Generar los puntos para GeoGebra
for i, point in enumerate(dodecahedron, 1):
    print(f'Punto{i} = ({point[0]}, {point[1]}, {point[2]})')
