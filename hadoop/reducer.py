#!/usr/bin/env python
"""reducer.py"""

# k-means reducer
# by Theodoros Plessas, 8160192
# Created in the scope of the "Big Data Management Systems" class

import sys

# Storage space for map results
# Format: [[<center_id>, <x_sum>, <y_sum>, <n_observations>], ...]
mapresults = []

for line in sys.stdin:
  line = line.strip() # Remove newline character
  # Extract data
  data = line.split(',')
  x = float(data[0])
  y = float(data[1])
  center = int(data[2])
  
  # If the center exists in mapresults[] add line data
  # If not create entry
  flag = 0
  for cluster in mapresults:
    if cluster[0] == center:
      cluster[1] += x
      cluster[2] += y
      cluster[3] += 1
      flag = 1
  if flag == 0:
    mapresults.append([center, x, y, 1])

for cluster in mapresults:
  print(str(cluster[1]/cluster[3]) + ',' + str(cluster[2]/cluster[3]))
