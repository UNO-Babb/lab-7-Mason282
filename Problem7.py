#Problem7.py
#Project Euler problem 7

import NumberTests
from NumberTests import nthPrime
    
if __name__ == "__main__":
  print("Finding the 1001st prime number...")
  prime_10001 = NumberTests.nthPrime(10001)
  print("The 10001st prime number is: " + str(prime_10001))
  