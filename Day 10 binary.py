import math
import os
import random
import re
import sys

if __name__="__main__":
    n=int(input().strip()) #strip is used for removing front & back spaces
    count=0
    while n:
    n &= n<<1
    count +=1
    print(count)