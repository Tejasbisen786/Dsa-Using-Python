class Circle:
    def __init__(self,radius=None):
        self.radius=radius
        # print("Circle Radius:",self.radius)
    def setRadius(self,radius):
        self.radius=radius
    def getradius(self):
        print("Circle Radius is :",self.radius)
    def getArea(self):
        area=3.14*self.radius*self.radius
        print("Area is : ",area)
    def getCircumference(self):
        cicurm=2*3.14*self.radius
        print("Circumference is :",cicurm)
    





c1=Circle()
c1.setRadius(10)
c1.getradius()
c1.getArea()
c1.getCircumference()

    
        