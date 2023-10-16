class Person:
    def __init__(self,name=None,age=None):
        self.name=name,
        self.age=age
        
    def setName(self,name):
        self.name=name
    def setAge(self,age):
        self.age=age
    def show(self):
        print("Name is",self.name)
        print("Age is: ",self.age)


p1=Person("Pratiksha Pawar",18)
p1.setAge(18)
p1.setName("Tejas Bisen")
p2=Person()
p2.setAge(21)
p2.setName("Pratiksha Pawar")
p1.show()
p2.show()
