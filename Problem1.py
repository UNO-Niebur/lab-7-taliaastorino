#Project Euler Problem 3

import NumberTests

def main():
  num = 600851475143
  largest = 0
  
  for i in range(2, int(num ** 0.5) + 1):
    if num % i = 0:
      if NumberTests.isPrime(i):
        largest = i

      other = num // i
      if NumberTests.isPrime(other):
        largest = other
        
  print(largest)


if __name__ == '__main__':
  main()
