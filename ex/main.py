import argparse
from colorama import Fore, Back, Style
from myfunctions import isPerfect

def main(): 
    parser =argparse.ArgumentParser(description='djajajaja')
    parser.add_argument('-mn', '--maximum_number', type=int, help='max number.')
    parser.add_argument('-n', '--name', type=str, help=' A name to print.', required ='false',default='Antonio')

    args=vars(parser.parse_args())
    print(args)

    #if args('say_hello')

    print('Hi ' + args(name) +"!!!\nStarting to compute perfect numbers up to "+str(args)['maximun_number'])


    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number '+ str(i) +' has dividers ')
            
            
    

if __name__ == "__main__":
    main()