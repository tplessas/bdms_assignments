#!/usr/bin/env python3

# k-means clustering dataset generator
# by Theodoros Plessas, 8160192
# Created in the scope of the "Big Data Management Systems" class
#
# USAGE: ./datagen.py <centers_file> (-v) (Show visualizations of data at finish time)
# Input: File (as command line argument) containing the coordinates
# of an arbitrary number of centers in the form "x,y", separated by line breaks.
# Output: (400k * <number of centers>) data points in STDOUT, redirect to file for further usage.

import numpy
import sys
import random
from matplotlib import pyplot as plt
from scipy.stats import skewnorm

# Load centers from file function
# Input: file name (command line argument)
# Output: [(x1,y1), (x2,y2) ...]
def load_centers(filename):
  centers = []
  
  # Read line, extract centers and store as tuples in centers[]
  file = open(filename, 'r')
  for line in file:
    line = line.strip() # Remove newline character
    coordinates = line.split(',')
    centers.append((float(coordinates[0]), float(coordinates[1])))
  
  file.close()
  del file
  return centers

# Load centers and make print not truncate results
centers = load_centers(sys.argv[1])
numpy.set_printoptions(threshold=sys.maxsize)

points = []
for center in centers:
  # Generate 800k right skewed distances (a = 5), twice the amount of points per center
  distances = skewnorm.rvs(5, size = 800000)
  for i in range(0, 800000, 2):
    # Use random distances to place points around centers
    x = center[0] + [-1,1][random.randrange(2)] * distances[i]
    y = center[1] + [-1,1][random.randrange(2)] * distances[i + 1]
    points.append((x, y))

for point in points:
  print(str(point[0]) + ',' + str(point[1]))
  
# Produce visualizations if argument passed
if sys.argv[2] == '-v':
  x, y = zip(*points)
  plt.scatter(x, y)
  plt.show()
