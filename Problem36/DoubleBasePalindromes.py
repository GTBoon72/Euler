def __isPalindrome(x):
  if x==x[::-1]:
    return True
  return False

def isPalindromeInBothBases(n: int):
  if __isPalindrome(bin(n).replace("0b", "")) and __isPalindrome(str(n)):
    return True
  return False

def PalindromesInBothBases(maximum: int):
  if not 0<maximum<10**7+1:
    raise ValueError("Input should be an integer between 0 and 10**7")
  PiBB=[]
  for i in range(1,maximum):
    if isPalindromeInBothBases(i):
      PiBB.append(i)
  return PiBB

def main():
  print("The sum of all palindromes in base2 and base10 below 1 million, is: " +
    str(sum(PalindromesInBothBases(10**6))))

if __name__ == '__main__':
    main()