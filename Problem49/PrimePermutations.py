from itertools import permutations

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

def __iList(i):
  return [i+x*3330 for x in range(3)]

def __iPerm(x):
  return [''.join(y) for y in list(permutations(str(x)))]

def validPermutations(power: int):
  if not 0<power<5:
    raise ValueError("Input should be an integer between 0 and 5")
  valid=[]
  for i in range(10**power-2*3330):
    i_list=__iList(i)
    if all(__isPrime(y) for y in i_list) and all(str(x) in __iPerm(i) for x in i_list):
      valid.append(list(str(z) for z in i_list))
  return valid

def main():
  print("The second concatenated sequence of primes below 10**4 that are permutations of each other, is : " +
    ''.join(validPermutations(4)[1]))

if __name__ == '__main__':
    main()