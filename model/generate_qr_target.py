#!/usr/bin/env python3

# To execute this script, the python module path must include the directory
# containing the Choreonoid python modules.
# Choreonoid python module directory usually exists at ${PREFIX}/lib/choreonoid-x.x/python.
# The python module path can be added by setting the environmental variable PYTHONPATH.

from math import *

name = "Target1"
qrcodeimage = "QR5.png"
radius = 0.005
height = 0.100
thickness = 0.001
baseHeight = 0.001
halfMarkerSize = cos(radians(45)) * (radius - thickness / 2.0)
resolution = 16

header = '''\
format: ChoreonoidBody
formatVersion: 1.0
angleUnit: degree
name: {name}

links:
  -
    name: QR-BASE
    jointType: fixed
    elements:
      - # QR code marker
        type: Visual
        shape:
          geometry:
            type: IndexedFaceSet
            coordinate: [
               {h:.4},  {h:.4}, {b},
              -{h:.4},  {h:.4}, {b},
              -{h:.4}, -{h:.4}, {b},
               {h:.4}, -{h:.4}, {b} ]
            coordIndex: [ 0, 1, 2, 3, -1 ]
            texCoord: [
              1, 1,
              0, 1,
              0, 0,
              1, 0 ]
            texCoordIndex: [ 0, 1, 2, 3, -1 ]
          appearance:
            texture:
              url: "resource/{image}"
      - # Base
        type: Shape
        rotation: [ 1, 0, 0, 90 ]
        translation: [ 0, 0, {halfBaseHeight} ]
        geometry:
          type: Cylinder
          radius: {baseRadius:.4}
          height: {baseHeight}
'''

print(header.format(
    name = name,
    h = halfMarkerSize,
    b = baseHeight + 0.001,
    image = qrcodeimage,
    halfBaseHeight = baseHeight / 2,
    baseRadius = radius * 1.2,
    baseHeight = baseHeight
    ))

box_description = '''\
      - # Cylinder wall {index}
        type: Shape
        rotation: [ 0, 0, 1, {theta:.7} ]
        translation: [ {x:.5}, {y:.5}, {z:.5} ]
        geometry:
          type: Box
          size: [ {sx:.7}, {sy:.7}, {sz:.7} ]
'''

t2 = 2.0 * pi / resolution / 2.0;
length = 2.0 * (radius * tan(t2) + (thickness / 2.0) * tan(t2));

for i in range(resolution):
    theta = 360.0 * i / resolution
    print(box_description.format(
        index = i + 1,
        theta = theta,
        x = radius * cos(radians(theta)),
        y = radius * sin(radians(theta)),
        z = height / 2 + baseHeight,
        sx = thickness,
        sy = length,
        sz = height
        ))
       
