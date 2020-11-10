from typing import List

def __nextPentagon(n: int):
  return int(0.5*n*(3*n-1))

def PentagonNumbers():
  Pentagons=[1,5,12]
  counter=1
  while True:
    for p in range(counter-1):
      while Pentagons[counter]+Pentagons[p]>max(Pentagons):
        Pentagons.append(__nextPentagon(len(Pentagons)))
      if Pentagons[counter]+Pentagons[p],Pentagons) and __isPentagon(Pentagons[counter]-Pentagons[p],Pentagons):
        return Pentagons[counter]-Pentagons[p]
    counter+=1

def main():
  print("The difference between the first pair of pentagonal numbers, for which both sum and difference are pentagonal, is: " +
    str(PentagonNumbers()))

if __name__ == '__main__':
    main()