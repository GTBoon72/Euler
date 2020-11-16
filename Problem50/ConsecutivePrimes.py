import numpy as np
from typing import List

def __isPrime(n: int):
  if n<=3:
    return n > 1
  if n%2==0 or n%3==0:
    return False

  i=5
  while i*i<=n:
    if n%i==0 or n%(i+2)==0:
      return False
    i+=6

  return True

def __next_prime(primes: List[int]):
  i=primes[-1]+2
  while not all(i%j!=0 for j in primes):
    i+=2
  return i

def __calculate_primes(c: int):
  primes=([2,3])
  while primes[-1]<c:
    primes.append(__next_prime(primes))
  return primes[:-1]

def ConsecutivePrimes(maximum: int):
  if not 5<maximum<10**7:
    raise ValueError("Input should be an integer between 5 and 10**7")
  primes=__calculate_primes(maximum/2)
  CP=np.zeros(maximum+1,dtype=int)
  for i in range(len(primes)-2):
    j=0
    primeSum=primes[i]
    while primeSum<maximum:
      if __isPrime(primeSum) and CP[primeSum]<=j:
        CP[primeSum]=j
      j+=1
      primeSum=sum(primes[i:i+j])
  return [max(CP),np.argmax(CP)]


def main():
  CP=ConsecutivePrimes(10**6)
  print("The largest amount of consecutive primes summing up to another prime below 10**6, is: " +
    str(CP[0]) + ", summing up to " + str(CP[1]))

if __name__ == '__main__':
    main()