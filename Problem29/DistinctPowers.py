import numpy as np

def Powers(a: int, b: int):
  if (a < 2 or b < 2):
    raise ValueError('This function only accepts 2 integers, both larger than 1')
  pow=[]
  for i in range(2,a+1):
    for j in range(2,b+1):
      pow.append(i**j)
  return(len(np.unique(np.array(pow))))

def main():
  print('The number of unique powers with a,b<=100 is: '+ str(Powers(100,100)))

if __name__ == '__main__':
    main()