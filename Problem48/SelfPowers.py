def selfPowers(x: int):
  if not 0<x<10**4:
    raise ValueError("Input should be integer between 0 and 10.000")
  return sum([x**x for x in range(x+1)])-1

def main():
  print("The last 10 digits of the sum of 1**1, 2**2, ... 1000**1000, is: " +
    str(selfPowers(1000))[-10:])

if __name__ == '__main__':
    main()