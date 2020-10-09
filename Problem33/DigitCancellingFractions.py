from math import gcd

def __cancelEqualDigits(n: int, d: int):
  x = sorted(str(n))
  y = sorted(str(d))
  return [[i,j] for i, j in zip(x,y) if i!=j]

def __isValidFraction(n: int, d: int):
  resp=__cancelEqualDigits(n,d)
  if len(resp)==1:
    if (int(resp[0][0])/int(resp[0][1]))==n/d:
      return True
  return False

def main():
  nprod=1
  dprod=1
  for i in range(10,50):
    for j in range(50,100):
      if not (i%10==0 or j%10==0):
        if __isValidFraction(i,j):
          nprod *= i
          dprod *= j
  highest_common_term=gcd(nprod,dprod)
  print("The denominator of the product of all 2-digit fractions where a digit can be removed from nominator and denominator, is: " +
    str(int(dprod/highest_common_term)))

if __name__ == '__main__':
    main()