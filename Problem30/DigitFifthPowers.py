def SumOfDigitPowers(powr: int):
  if not 1<powr<7:
    raise ValueError("This function expects an integer between 1 and 7")
  results=[]
  for i in range(2,10**(powr+1)):
    if i==sum([int(j)**powr for j in list(str(i))]):
      results.append(i)
  return str(sum(results))

def main():
  print("The sum of the numbers that are equal to the 5th power of their digits is: " +
    SumOfDigitPowers(5))
  print("Disclaimer: this has been tested up to 10**6")

if __name__ == '__main__':
    main()