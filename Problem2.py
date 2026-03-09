#Problem2.py
#Project Euler problem 4

def isPalindrome(n):
  s = str(n)
  if s == s[::-1]:
    return True
  else:
    return False

def main():
  largest = 0
 
  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i * j
    
      if isPalindrome(product):
        if product > largest:
          largest = product
  
  print(largest) # final answer

if __name__ == '__main__':
  main()
