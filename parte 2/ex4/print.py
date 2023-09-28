
import readchar

def printAllCharsUpTo():
   a=[]
   print('Press a key to read char')
   key= readchar.readkey()

   print('Pressed key is ', key)
   max_number = ord(key)

   print("Corresponding number is ", max_number)

   chars_to_print =[]
   for i in range (32,max_number):
    chars_to_print.append(chr(i))
   print('<->',chars_to_print)

def readAllUpTo(stop_char):
   i=1;
   char =[]
   while True :
    char.append(readchar.readkey())
    print(char[-1])
    if char[i]== stop_char:
     break


def countNumbersUpto(stop_char):

    print('Start typing')
  
    keys=[]
    while True:
        key=readchar.readkey()
        keys.append(key)
        print('You typed ', key)

        if key == stop_char:
          break
        
    print(keys)

    n_numeric=0
    

    for key in keys:
      if key.isnumeric():
        n_numeric += 1

    print('You pressed on ' + str(n_numeric) + ' numeric keys')    


    