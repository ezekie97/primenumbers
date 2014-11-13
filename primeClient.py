import rpyc

class primesClient:
    """ establish connection"""
    def __init__(self):
        print("Connecting")
        self.c = rpyc.connect("150.250.211.136",12345)
        print("Connected")

    """ reach to primes service"""
    def getPrimesService(self):
        num = int(input("Please type a number: "))
        return self.c.root.findPrimes(num)
client = primesClient()
client.getPrimeService()
    

    
