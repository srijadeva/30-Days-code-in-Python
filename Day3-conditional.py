import math
import os
import random
import re
import sys

if __name__="__main__":
    print("Not Weird"*(int(input().strip())in{2,4}| set (range(22,101,2)))+'Weird')