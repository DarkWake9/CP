#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    
    def __init__(self, length = 0, breadth = 0):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius)**2

if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()
