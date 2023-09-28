
from colorama import Fore, Back, Style

maximum_number = 100
def getDividers(value):
    dividers =[]
     
   
    for i in range(1,value):
        if value%i==0:
            dividers.append(1)
    return dividers

def isPerfect(value):
    dividers = getDividers(value)
    return value == sum(dividers)



