class Circle:
    def __init__(self,radius):
        self.radius=radius

    def peri(self):
        print("Perimeter is ",self.radius*2*3.14)
    
    def area(self):
        print("Area is ",3.14*self.radius**2)

a= Circle(1)
a.peri()
a.area()