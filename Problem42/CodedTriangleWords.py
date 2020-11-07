import csv

n=1
Triangles=[1]

def wordValue(word: str):
  if not all(x.isalpha() for x in word):
    raise TypeError("Input should be a string of letters")
  wV=[ord(ch)-64 for ch in sorted(word.upper())]
  return sum(wV)

def __nextTriangle():
  global n
  global Triangles
  n+=1
  Triangles.append(int(0.5*n*(n+1)))

def __isTriangle(word: str):
  if wordValue(word) in Triangles:
    return True
  return False

def __readWords():
  with open(r'.\\Problem42\\words.txt') as wordfile:
    words=[]
    for row in csv.reader(wordfile, delimiter=',', quotechar='"'):
      words+=row
  return words

def main():
  global Triangles
  counter=0
  for word in __readWords():
    while wordValue(word)>max(Triangles):
      __nextTriangle()
    if __isTriangle(word):
      counter+=1
  print("The number of words of which the sum of the letter values is a triangle numbers, is: " +
    str(counter))

if __name__ == '__main__':
    main()