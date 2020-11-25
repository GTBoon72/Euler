def permutedMultiples(x: int):
  if not 1<x<10:
    raise ValueError("Input should be an integer between 1 and 10")
  counter=0
  while True:
    counter+=1
    if all(sorted(str(counter))==sorted(str(i*counter)) for i in range(2,x+1)):
      return counter

def main():
  print("The smallest positive integer x that contains the same digits as [2,3,..,6]*x, is: " +
    str(permutedMultiples(6)))

if __name__ == '__main__':
    main()
