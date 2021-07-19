#!/usr/bin/env python
"""mapper.py"""

# k-means mapper
# by Theodoros Plessas, 8160192
# Created in the scope of the "Big Data Management Systems" class

import sys
from math import sqrt

# Euclidean distance (2D) calculation function
# Input: x, y of two points
# Output: Euclidean distance between points
def euclidean_distance(x1, y1, x2, y2):
  return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Load centers from file function
# Input: file name (command line argument)
# Output: [(x1,y1), (x2,y2) ...]
def load_centers(filename):
  centers = []
  
  # Read line, extract center coordinates and store as tuples
  file = open(filename, 'r')
  for line in file:
    line = line.strip() # Remove newline character
    coordinates = line.split(',')
    centers.append((float(coordinates[0]), float(coordinates[1])))
  
  file.close()
  del file
  return centers

# Load centers
centers = load_centers(sys.argv[1])

for line in sys.stdin:
  line = line.strip() # Remove newline character
  # Extract coordinates in float form
  coordinates = line.split(',')
  x = float(coordinates[0])
  y = float(coordinates[1])
  
  # Calculate distance from every center to select nearest one
  euclidean_center = 0
  center_distance = 999999999
  for center in centers:
    distance = euclidean_distance(x, y, center[0], center[1])
    if center_distance > distance:
      euclidean_center = centers.index(center)
      center_distance = distance

  # Reducer takes it from here
  print(str(x) + ',' + str(y) + ',' + str(euclidean_center))
