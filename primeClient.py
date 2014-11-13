import rpyc

class primesClient:
    """ establish connection"""
    def __init__(self):
        self.c = rpyc.connect("10.0.2.15",12345)

    """ reach to primes service"""
    def getPrimesService(self):
        num = int(input("Please type a number: "))
        return self.c.root.findPrimes(num)
    
    
