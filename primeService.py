#!/usr/bin/env python
__author__ = "William Ezekiel"

__date__ = "12 November 2014"

__version__ = "1.1"

import rpyc

class primesService(rpyc.Service):
    """ provided a service that finds all prime numbers <= a given number"""

    def on_connect(self):
        print("Connected")
        pass

    def on_disconnect(self):
        print("Bye")
        pass
      
    def exposed_findPrimes(self,num):
        """find all prime numbers <= to a given number
        :param num: the maximum in the range of numbers
        :returns: A string of the the numbers <= max_number
        """
        primes = []
        for i in range(1,num+1):
            if self.isPrime(i):
                primes.append(i)
        # sub string to remove brackets
        return str(primes)[1:-1]
    
    def isPrime(self,num):
        """Check if a number is prime
        :param num: the number to be checked. 
        :returns: true if the number is prime
        """
        # if 1 2 or 3.
        if num<=3:
            return num>=2
        
        # check if a number is even or
        # if it is a special case like
        # 9 or 15 that fails in the following
        # loop
        
        if num%2 == 0 or num%3 == 0:
            return False
        
        # starting from 5, we check if a number
        # is divisible by any of the lesser
        # odd numbers.
        # We go until the square root of number+1 since
        # if we don't find a divisor below or equal to the
        # square root, we won't find one above the square root.
        
        for i in range(5,int(num**0.5)+1,2):
            if num % i == 0:
                return False
        return True
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    print("Starting Server")
    t = ThreadedServer(primesService, port = 12345)
    t.start()
