import numpy as np

def __create_sieve(maximum: int):
  sieve=np.zeros((maximum),dtype=int)
  return sieve

def IntegerRightTriangles(sumOfSides: int):
  if not 0 < sumOfSides < 10**4:
    raise ValueError("Input should be an integer between 0 and 10**4")
  sieve=__create_sieve(sumOfSides)
  for i in range(1,sumOfSides):
    for j in range(1,sumOfSides):
      p=i+j+np.sqrt(i**2+j**2)
      if (i<j) and (p - int(p)==0) and (p<sumOfSides):
        sieve[int(p)]+=1
  return max(enumerate(sieve), key=(lambda x:x[1]), default = -1)[0]

def main():
  print("The triangle sum having the highest number of ways to create it, is: " +
    str(IntegerRightTriangles(1000)))

if __name__ == '__main__':
    main()