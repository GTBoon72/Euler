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

def __getDigits(x: int):
  Digits=[]
  for i in range(9):
    if str(x).count(str(i))>0:
      Digits.append(i)
  return Digits

def __sizeOfFamily(prime: int, digit: int):
  sOF=0
  PrimesInFamily=[]
  for i in range(10):
    nr=str(prime).replace(str(digit),str(i))
    if __isPrime(int(nr)) and nr[0]!='0':
      sOF+=1
      PrimesInFamily.append(int(nr))
  return [sOF,PrimesInFamily]

def firstPrimeInFamilyOfSize(FamilySize: int):
  if not 0<FamilySize<10:
    raise ValueError("Input should be an integer between 0 and 10")
  for prime in __primeGenerator():
    for digit in __getDigits(prime):
      if __sizeOfFamily(prime, digit)[0]==FamilySize:
        return [prime,__sizeOfFamily(prime, digit)[1]]

def main():
  print("The first prime that has a set of 8 primes when replacing any copy of a digit, is: " +
    str(firstPrimeInFamilyOfSize(8)[0]))

if __name__ == '__main__':
    main()