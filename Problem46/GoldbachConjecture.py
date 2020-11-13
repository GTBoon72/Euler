from typing import List
from itertools import product
import math

def __next_prime(primes: List[int]):
  i=primes[-1]+2
  while not all(i%j!=0 for j in primes):
    i+=2
  return i

def calculate_first():
  primes=([2,3])
  i=1
  while True:
    i+=2
    while primes[-1]<i:
      primes.append(__next_prime(primes))
    if i not in primes:
      if not any(i==j+2*k**2 for j,k in list(product(*[primes,[x for x in range(1,int(math.sqrt(i)))]]))):
        return i

def main():
  print("The first odd number that does not comply to Goldbach's rule, is : " +
    str(calculate_first()))

if __name__ == '__main__':
    main()