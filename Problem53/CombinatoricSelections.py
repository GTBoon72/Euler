from operator import mul
from fractions import Fraction
from functools import reduce

def __nCk(n,k):
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

def validCombinations(n: int, minimum: int):
  if not 0<n<1000 or not 0<minimum<10**9:
    raise ValueError("Input should be 2 integers, smaller than 1000 and 10**9 respectively")
  count=0
  for i in range(1,n+1):
    for r in range(1,i):
      #combinations from itertool does the same, but produces memoryError for so many values
      #nCk just gives the amount of combinations, rather than the combinations themselves
      #this function was found on the internet
      if __nCk(i,r)>minimum:
        count+=1
  return count

def main():
  print("The number of values where n over r is greater than 10**6, and n<=100, is: " +
    str(validCombinations(100,10**6)))

if __name__ == '__main__':
    main()