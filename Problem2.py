#Problem2.py
#Project Euler problem 4
#Name: Talia Astorino
#Date: 03/08/2026
#Purpose: Finds the largest palindrome made from the product of two 3-digit numbers.
#The program multiplies pairs of numbers from 100 to 999 and checks if the product is a palindrome by comparing the number to its reverse.
#Runtime is moderate because the program checks many combinations of numbers, but I optimized it by changing the range.

def isPalindrome(n):
  s = str(n)
  if s == s[::-1]:
    return True
  else:
    return False

def main():
  largest = 0
 
  for i in range(100, 1000):
    for j in range(i, 1000):
      product = i * j
    
      if isPalindrome(product):
        if product > largest:
          largest = product
  
  print(largest) # final answer

if __name__ == '__main__':
  main()
