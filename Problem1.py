#Project Euler Problem 3
#Name: Talia Astorino
#Date: 03/08/2026
#Finds the largest prime factor of the number 600851475143.
#The program checks possible factors of the number and uses the isPrime() function from NumberTests.py to check if the factor is prime.
#Runtime is reasonable. The program only checks factors up to the square root of the number to decrease amount of numbers that need to be checked.

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
