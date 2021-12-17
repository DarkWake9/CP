#Task
#'''Function to print the average of any number of arguments subject to costraints'''
#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
def avg(*argv):
    l = len(argv)
    ver = all(b >= -100 and b <= 100 for b in argv) 
    if l <= 100 and l > 0 and ver:
        a=0
        for b in argv:
            a+=b
        a/=len(argv)
        return a
    elif ver != True:
        print("Elements out of range")
    else:
        print("List is empty or too long")        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()