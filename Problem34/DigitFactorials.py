from math import factorial

def __calculateDigits():
  n=1
  while n*factorial(9) > 10**n:
    n+=1
  return n

def sumDigitFactorial(x: int):
  if not x>0:
    raise ValueError("Input should be an integer larger than zero")

  return sum([factorial(int(i)) for i in sorted(str(x))])

def __getNumbers():
  result=[]
  for x in range(3,10**__calculateDigits()):
    if x==sumDigitFactorial(x):
      result.append(x)
  return result

def main():
  print("The sum of all numbers that equal the sum of the factorial of its digits, is: " +
    str(sum(__getNumbers())))

if __name__ == '__main__':
    main()