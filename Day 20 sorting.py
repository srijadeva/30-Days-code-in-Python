import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    swaps = 0
    not_solved = True

    while not_solved:
         for i in range(n-1):
             if a[i] > a[i+1]:
                swaps += 1
                a[i],a[i+1] = a[i+1],a[i]
                break
             if i == n-2:
                not_solved = False
            
print("Array is sorted in {} swaps.".format(swaps))
print("First Element:", a[0])
print("Last Element:", a[-1])