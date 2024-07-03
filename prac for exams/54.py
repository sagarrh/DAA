
class Zerocannotbedenominator(Exception):
    def __init__(self,b,d):
        super().__init__("Product of b and d is zero")



def calculate(b,d):
    if b*d==0:
        raise Zerocannotbedenominator(b,d)
    else:
        return b*d


b=int(input("b"))
d=int(input("d"))   

print(calculate(b,d))