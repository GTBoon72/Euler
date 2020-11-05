from typing import List

def __isPandigital(a: List):
  if sorted(a)==['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    return True
  return False

def Pandigital_Multiples():
  PanMultiples=[]
  for i in range(2,10**4):
    concat_multiples=[]
    j=0
    while len(''.join(concat_multiples))<9:
      j+=1
      concat_multiples.append(str(i*j))
    if __isPandigital(''.join(concat_multiples)):
      PanMultiples.append(''.join(concat_multiples))
  return PanMultiples

def main():
  print("The largest pandigital number that can be constructed from multiples is: " +
    str(max([int(x) for x in Pandigital_Multiples()])))

if __name__ == '__main__':
    main()