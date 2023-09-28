import readchar
from colorama import Fore, Back, Style

def countNumbersUpto(stop_char):

    print('Start typing')
  
    keys=[]
    while True:
        key=readchar.readkey()
        keys.append(key)
        print('You typed ', key)

        if key == stop_char:
          break

    n_numeric=0
    
    print(keys)
    a=[]
    for key in keys:
      if key.isnumeric():
        n_numeric += 1
        a.append(key)
    print('You pressed on ' + str(n_numeric) + ' numeric keys')    
    a.sort()
    print(a)

    d_keys={}

    i=0
    for key in keys:
       d_keys[i]=key
       i= i +1
    print('d_keys = '+ str(d_keys))

    numeric2= [x for x in keys if x.isnumeric()]
    print(str(numeric2))

    for idx_key, key in keys:
       print(Fore.RED + str(idx_key)+ Style.RESET_ALL + Fore.GREEN +': key pressed is: ' + Style.RESET_ALL + Fore.MAGENTA+ key + Style.RESET_ALL)

def main():
    countNumbersUpto('x')

if __name__ == '__main__':
    main()