from itertools import permutations
import numpy as np

def __create_sieve(r: int,c: int):
  sieve=np.zeros((r,c),dtype=int)
  return sieve

def getPandigitals():
  digits='0123456789'
  perm=[''.join(x) for x in list(permutations(digits))]
  sieve=__create_sieve(len(perm),7)
  n=1
  for i in [2,3,5,7,11,13,17]:
    for p in range(len(perm)):
      if int(perm[p][n:n+3])%i==0 and perm[p][0]!='0':
        sieve[p,n-1]=1
    n+=1
  return [int(p) for p in [perm[int(ind)] for ind in [i for i,x in enumerate(sieve) if all(x==1)]]]

def main():
  print("The sum of all Pandigitals with subsets divisible by primes, is: " +
    str(sum(getPandigitals())))

if __name__ == '__main__':
    main()