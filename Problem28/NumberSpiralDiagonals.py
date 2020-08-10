def NumbersOnDiagonal(width: int):
  if (width%2 == 0 or width <= 1):
    raise ValueError('This function accepts only uneven integers higher than 1')
  NoD=[1]
  for w in range(3,width+1,2):
    for i in range(4):
      NoD.append(w**2-i*(w-1))
  return(sum(NoD))

def main():
  print('The sum of the numbers on the diagonals of a number spiral of 1001x1001 equals: ' +
    str(NumbersOnDiagonal(1001)))

if __name__ == '__main__':
    main()