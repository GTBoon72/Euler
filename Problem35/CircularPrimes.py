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

def __primeGenerator(maximum: int):
  for i in range(3,maximum,2):
    if __isPrime(i):
      yield i

def __primeRotations(digits: str):
  generator={digits[x:]+digits[:x] for x in range(len(digits))}
  for i in generator:
    yield ''.join(i)

def circularPrimes(x: int):
  if not 1<x<10**7:
    raise ValueError("Input should be an integer between 1 and 10 million")
  circular_primes=[2]
  for prime in __primeGenerator(x):
    prime_rotations=[]
    for prime_rotation in __primeRotations(str(prime)):
      prime_rotations.append(0)
      if __isPrime(int(prime_rotation)):
        prime_rotations[-1]=1
    if sum(prime_rotations)==len(prime_rotations):
      circular_primes.append(prime)
  return circular_primes

def main():
  print("The number of circular primes below 1 million, is: " + str(len(circularPrimes(10**6))))

if __name__ == '__main__':
    main()
