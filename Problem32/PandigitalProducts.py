from numpy import unique
def __isPandigitalProduct(a: int, b: int):
  if sorted(str(a)+str(b)+str(a*b))==['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    return True
  return False

def UniquePandigitalProducts():
  PandigitalProducts=[]
  for i in range(1,500):
    for j in range(100,2000):
      if(__isPandigitalProduct(i,j)):
        PandigitalProducts.append(i*j)
  return unique(PandigitalProducts)

def main():
  print("The sum of the unique Pandigital Products is: " + str(sum(UniquePandigitalProducts())))

if __name__ == '__main__':
    main()