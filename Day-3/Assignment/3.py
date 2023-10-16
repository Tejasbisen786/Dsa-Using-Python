class Rectangle:
   def __init__(self,len=None,brd=None):
      self.len=len
      self.brd=brd
      print("Length is :",self.len)
      print("Bradth is :",self.brd)
   def SetDimensions(self,len,brd):
      self.len=len
      self.brd=brd
   def showDimension(self):
      print("Length is :",self.len)
      print("Width is :",self.brd)
   def getArea(self):
      area=self.len*self.brd
      print("Area of rectangle is:",area)
    



r1=Rectangle(23,45)
r2=Rectangle(10,20)
r2.showDimension()
r2.getArea()
r1.getArea()

