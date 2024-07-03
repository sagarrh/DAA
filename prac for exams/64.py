class String:
    def getstring(self,string):
        self.string=string
    
    def printstring(self):
        print(self.string.upper())

s=String()
s.getstring("ahahah")
s.printstring()