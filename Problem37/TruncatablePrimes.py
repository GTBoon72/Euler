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

def __primeGenerator():
  yield 2
  for i in range(3,10**10,2):
    if __isPrime(i):
      yield i

def truncatablePrimes(amount:int):
  if not 0<amount<25:
    raise ValueError("The input should be an integer between 0 and 25")
  TruncatablePrimes=[]
  for prime in __primeGenerator():
    if len(str(prime))>1:
      PrimeIsTruncatable=0
      for i in range(1,len(str(prime))):
        if not __isPrime(int(str(prime)[i:])):
          PrimeIsTruncatable=1
        if not __isPrime(int(str(prime)[:-i])):
          PrimeIsTruncatable=1
      if PrimeIsTruncatable==0:
        TruncatablePrimes.append(prime)
      if len(TruncatablePrimes)==amount:
        return TruncatablePrimes

def main():
  print("The sum of all truncatable primes is: " + str(sum(truncatablePrimes(11))))

if __name__ == '__main__':
    main()
