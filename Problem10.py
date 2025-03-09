#Problem7.py
#Project Euler problem 7

import NumberTests
from NumberTests import sumOfPrimes
    
if __name__ == "__main__":
  print("Calculating sum of primes below 2000000...")
  sum_primes = NumberTests.sumOfPrimes(2000000)
  print("The sum of all primes below 2,000,000 is: " + str(sum_primes))
  