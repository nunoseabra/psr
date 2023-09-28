from cmath import sqrt

maximum_number = 100
def getDividers(value):
    dividers =[]
    for i in range (1, round(value/2 +1)):
        if value%i== 0:
            dividers.append(i)
    return dividers

def isPerfect(value):
    dividers = getDividers(value)
    return value == sum(dividers)

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number '+ str(i) +' has dividers ')
            
            
    

if __name__ == "__main__":
    main()