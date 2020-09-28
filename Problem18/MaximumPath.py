#Didn't think this one up myself. Found the code here:
#https://www.pybloggers.com/2015/05/project-euler-18-maximum-path-sum-i/

import urllib.request

def __construct_triangle():
  req = urllib.request.Request("https://projecteuler.net/problem=18")
  response = urllib.request.urlopen(req)
  the_page = response.read()
  the_page_string = the_page.decode("utf-8")
  counter = the_page_string.find("75<br />")

  triangle = []
  row = []

  while(counter < len(the_page_string)):
    # add number to list
    row.append(int(the_page_string[counter:counter+2]))
    counter += 2

    if(the_page_string[counter] == " "):
      counter += 1
    elif(the_page_string[counter:counter+6] == "<br />"):
      counter += 8 # +2 for n
      triangle.append(row)
      row = []
    elif(the_page_string[counter:counter+4] == "</p>"):
      triangle.append(row)
      break
  return(triangle)

def solve_triangle():
  triangle=__construct_triangle()
  depth = len(triangle)
  for i in range(depth-2,-1,-1):
    for j in range(0,len(triangle[i])):
      triangle[i][j] += max([triangle[i+1][j], triangle[i+1][j+1]])
  return(triangle[0][0])

def main():
  print("The maximum sum of numbers in the triangle is: " + str(solve_triangle()))

if __name__ == '__main__':
    main()