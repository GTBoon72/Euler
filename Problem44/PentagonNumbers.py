Pentagons=[1,5,12]

def __nextPentagon():
  global Pentagons
  n=len(Pentagons)
  Pentagons.append(int(0.5*n*(3*n-1)))

def __isPentagon(p: int):
  global Pentagons
  if p in Pentagons:
    return True
  return False

def PentagonNumbers():
  global Pentagons
  FoundOne=False
  counter=1
  while not FoundOne:
    for p in range(counter-1):
      while Pentagons[counter]+Pentagons[p]>max(Pentagons):
        __nextPentagon()
      if __isPentagon(Pentagons[counter]+Pentagons[p]) and __isPentagon(Pentagons[counter]-Pentagons[p]):
        return Pentagons[counter]-Pentagons[p]
        FoundOne=True
    counter+=1

def main():
  print("The difference between the first pair of pentagonal numbers, for which both sum and difference are pentagonal, is: " +
    str(PentagonNumbers()))

if __name__ == '__main__':
    main()