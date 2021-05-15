import math
import os
import random
import re
import sys

if __name__="__main__":
    n = int(input().strip())
    arr = int(map(input().rstrip().split()))
    print(''.join(map(str,reversed(arr))))