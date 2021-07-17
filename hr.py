import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())
    
    tip=(meal_cost*(meal_cost/100))*tip_percent
    tax=(tax_percent*(tax_percent/100))*tip_percent
    
    total_cost=meal_cost+tip+tax
    print(total_cost)


    solve(meal_cost, tip_percent, tax_percent)
