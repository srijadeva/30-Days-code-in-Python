import math
import os
import random
import re
import sys

def_solve(meal_cost,tip_percent,tax_percent):
       tip=meal_cost*tip_percent/100
       tax=meal_cost*tax_percent/100
       total_cost=meal_cost+tip+tax
       print(round(total_cost))

if __name__=='__main__':
    meal_cost=float(input().strip())
    tip_percent=int(input().strip())
    tax_percent=int(input().strip())
    solve(meal_cost,tip_percent,tax_percent)