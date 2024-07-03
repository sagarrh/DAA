class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def calculate_perimeter(self):
        return self.a+self.b+self.c
    
tri=Triangle(2,3,4)
perimeter=tri.calculate_perimeter()
print(perimeter)