import numpy as np

def __next_number(maximum: int):
  for i in range(1,10**maximum+1):
    yield i

def calcChampernowne(exponent: int):
  if not 0<exponent<8:
    raise ValueError("Input should be an integer between 0 and 8")
  Champernowne=''
  for nr in __next_number(exponent):
    if not len(Champernowne)>10**exponent:
      Champernowne+=str(nr)
    else:
      return Champernowne
  return Champernowne

def main():
  exponent=7
  Champernowne=calcChampernowne(exponent)
  digits=[Champernowne[(10**x)-1] for x in range(0,exponent)]
  print("The product of the digits in Champernowne's constant indexed at 10**0..10**7 is: " +
    str(np.prod([int(x) for x in digits])))

if __name__ == '__main__':
    main()