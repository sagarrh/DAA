class Power:
    def __init__ (self,a,b):
        self.a=a
        self.b=b
    
    def calc(self):
        ret=1
        while self.b > 0:
            ret=ret*self.a
            self.b=self.b-1
        return ret

a=Power(3,2)
print(a.calc())
            
        
