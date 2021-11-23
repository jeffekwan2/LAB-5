import math
import sys

def computeArea(radius):
    return math.pi * radius * radius
radius = float(input("Enter the radius in feet : "))
sys.stdout.write("The radius you provided was "+ format(radius,'.2f') + " feet amd the area is about "+ format(computeArea(radius),'.2f') + " sq feet")
