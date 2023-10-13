li=[12,3,4]
li.append(20)
# li.show()   # Attribute Eror
# print(li)

# class TEst:
#     #attribute

# class TestClass:
# def():

# class student:
#      x=120   # class Object Variable / Static Variable
#      print("value of x is : ",x)
     
# t1=student()
# t2=student()
# t1=student()


class Test:
    x=5
    def __init__(self,a,b):
        self.a=a
        self.b=b
        # print(a+b)
    def show(self):  # instance method
        print(self.a,self.b)
    @staticmethod 
    def f2():
        print("tejas")
    @classmethod
    def f3(cls):
        print(cls.x)

t1=Test(20,13)
t2=Test(15,23)
t1.show()
t2.show()


Test.f3()  # Class Obejct Ko refer kr rha hai
Test.f2()

