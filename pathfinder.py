import random
import string

def source_file():
  source_file = samples/elevation_small.txt
  with open({source_file}) as file:
    elevation_list = file.read()

def determine_source_file_size():
  width = 0
  height = 0
  for elevation in elevations:

def min_elevation(elevations):
  min_elevation = 250000
  for elevation in elevations:
    if elevation < min_elevation:
      min_elevation = elevation
  return min_elevation

def max_elevation(elevations):
  max_elevation = 0
  for elevation in elevations:
    if elevation > max_elevation:
      max_elevation = elevation
  return max_elevation

def avg_elevation(elevations):
  total_elevation = 0
  elevation_count = 0
  for elevation in elevations:
    total_elevation += elevation
    elevation_count +=1
  return total_elevation/elevation_count

def main():
  pass
#   min_elevation = min_elevation()

# main()