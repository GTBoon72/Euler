def __nextTriangle(t: int):
  n=t+1
  return int(0.5*n*(n+1))

def __nextPentagon(p: int):
  n=p+1
  return int(0.5*n*(3*n-1))

def __nextHexagon(h: int):
  n=h+1
  return int(n*(2*n-1))

def TPH(minimum):
  if not 0<minimum<10**9:
    raise ValueError("Input should be an integer between 0 and 10**9")
  Triangles=[1]
  Pentagons=[1]
  Hexagons=[1]
  while True:
    Triangles.append(__nextTriangle(len(Triangles)))
    while max(Triangles)>max(Pentagons):
      Pentagons.append(__nextPentagon(len(Pentagons)))
    while max(Triangles)>max(Hexagons):
      Hexagons.append(__nextHexagon(len(Hexagons)))
    if max(Triangles) in Pentagons and max(Triangles) in Hexagons and max(Triangles)>minimum:
      return max(Triangles)

def main():
  print("The first Triangle number higher than 40755, that is also a Pentagonal and a Hexagonal number, is: " +
    str(TPH(40755)))

if __name__ == '__main__':
    main()