import csv
from typing import List

def wordValue(word: str):
  if not all(x.isalpha() for x in word):
    raise TypeError("Input should be a string of letters")
  wV=[ord(ch)-64 for ch in sorted(word.upper())]
  return sum(wV)

def __nextTriangle(n: int):
  n+=1
  return int(0.5*n*(n+1))

def __isTriangle(word: str, Triangles: List):
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
  Triangles=[1]
  counter=0
  for word in __readWords():
    while wordValue(word)>max(Triangles):
      Triangles.append(__nextTriangle(len(Triangles)))
    if __isTriangle(word, Triangles):
      counter+=1
  print("The number of words of which the sum of the letter values is a triangle numbers, is: " +
    str(counter))

if __name__ == '__main__':
    main()