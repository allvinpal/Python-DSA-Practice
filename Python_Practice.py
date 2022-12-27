#Program to find the arc length of a circle.

#The input radius and center angle must be a float variables, the output should also be printed as a floating point value with 2 point precision. no other extra information should be printed except the arc length value to the stdout. (Assume PI = 3.14)


#Input (stdin)
#25
#50

#Output (stdout)
#21.81

import math
pi=3.14
def find_arc_length(radius, center_angle):
  arc_length = (2*pi*radius) * (center_angle / 360)
  return arc_length


radius = float(input())
center_angle = float(input())
arc_length = find_arc_length(radius, center_angle)
print( "%.2f" %arc_length)
