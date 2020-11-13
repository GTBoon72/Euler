from sympy import primefactors

def consecutiveNumbers(c: int):
  if not 0<c<5:
    raise ValueError("Input should be an integer between 0 and 5")
  counter=0
  while True:
    counter+=1
    if all(len(primefactors(counter+x))==c for x in range(c)):
      return counter

def main():
  print("The first of 4 consecutive numbers that have 4 distinct prime factors, is: " +
    str(consecutiveNumbers(4)))

if __name__ == '__main__':
    main()