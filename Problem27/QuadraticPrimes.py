def __isPrime(n: int):
  if n<=3:
    return n > 1
  if n%2==0 or n%3==0:
    return False

  i=5
  while i*i<=n:
    if n%i==0 or n%(i+2)==0:
      return False
    i+=6

  return True

def __primeGenerator():
  for i in range(5,100,6):
    if __isPrime(i):
      yield i

def qprimes():
  n_max_a=0
  b_max_a=0
  a_max=0
  for a in range(-1000,1000):
    n_max=0
    for b in range(5,1000,6):
      if __isPrime(b):
        n=0
        while __isPrime(n*n+a*n+b):
          n+=1
        if n>n_max:
          n_max=n
          b_max=b
    if n_max>n_max_a:
      n_max_a=n_max
      b_max_a=b_max
      a_max=a
  return(a_max,b_max_a,n_max_a)

def main():
  result=qprimes()
  print('Max number of primes is '+str(result[2])+' with a='+str(result[0])+' and b='+str(result[1]))
  print('The product of a and b equals '+str(result[0]*result[1]))

if __name__ == '__main__':
    main()