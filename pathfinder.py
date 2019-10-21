import random
import string
from PIL import Image


class Map:

  # def __init__():

  def get_elevation_list():
    with open("elevation_small.txt") as file:
      elevation_list = file.readlines()
    return elevation_list

  def get_elevations(elevation_list):
      elevations = [[int(elevation) for elevation in line.split()] for line in elevation_list]
      return elevations

  def min_elevation(elevations):
    min_elevation = 250000
    
    for each in elevations:
      for elevation in each:    
        # print(elevation, min_elevation)
        if elevation < min_elevation:
          min_elevation = elevation
    
    return min_elevation

  def max_elevation(elevations):
    max_elevation = 0
    for each in elevations:
      for elevation in each: 
        if elevation > max_elevation:
          max_elevation = elevation
    return max_elevation

  def map_color_data(min_elevation,max_elevation,elevations):
    row_color_values = []
    map_color_values = []
    for row in elevations:
      for elevation in row:
        color_value = int(((elevation - min_elevation)/max_elevation) * 255)
        row_color_values.append(color_value)
      # map_color_values.append(color_value,color_value,color_value,255)
      map_color_values.append(row_color_values)
      row_color_values = []
    return map_color_values

  def greedy_trail(elevations, map_image):
    x = 0
    # y = 0
    y = random.randint(0,600)
    current_point = (elevations[x][y])
    while x < 598:
      up = abs((elevations [x+1][y-1]) - current_point)
      right = abs((elevations [x+1][y]) - current_point)
      down = abs((elevations [x+1][y+1]) - current_point)
      smallest_change = min(up,right,down)
      if smallest_change == up:
        y -= 1
        x += 1
        if y < 0:
          break
        # print(x,y )
        map_image.putpixel((x,y), (0, 255, 0, 255))
        current_point = (elevations[x][y])
      if smallest_change == right:
  
        x += 1
        # print(x,y )
        map_image.putpixel((x,y), (0, 255, 0, 255))
        current_point = (elevations[x][y])
      if smallest_change == down:
        y += 1
        x += 1
        if y > 600:
          break
        # print(x,y )
        map_image.putpixel((x,y), (0, 255, 0, 255))
        current_point = (elevations[x][y])
      
      

  def draw_map():
    height = 600
    width = 600
    map_image = Image.new('RGBA', (width, height), color = (0,0,0,255))
    elevation_list = Map.get_elevation_list()
    elevations = Map.get_elevations(elevation_list)
    # print (elevation_list, elevations)
    min_elevation = Map.min_elevation(elevations)
    max_elevation = Map.max_elevation(elevations)
    # print(min_elevation.type())
    # print(max_elevation.type())
    map_color_values = Map.map_color_data(min_elevation,max_elevation,elevations)
    # print(map_color_values)
    for y, row in enumerate(map_color_values, 0):
      for x, color_value in enumerate(row, 0):
        map_image.putpixel((x,y), (color_value, color_value, color_value, 255))
    Map.greedy_trail(elevations, map_image)
    map_image.save('output.png')






    # pass

# pathfinder.run()
Map.draw_map()
# pathfinder()