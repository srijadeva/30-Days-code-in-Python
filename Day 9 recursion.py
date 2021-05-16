import math
import os
import random
import os
import sys
def factorial(n):
    if n<=1:
     return 1
    else:
        result = n* factorial(n-1)
if __name__="__main__":
    fptr=open(os.environ['OUTPUT_PATH'],'w')
    n=int(input().strip())
    result = factorial(n)
    fptr.rite(str(rsult)+'\n')
    fptr.close()