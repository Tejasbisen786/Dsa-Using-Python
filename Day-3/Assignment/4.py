class Book:
 def __init__(self,bookid=0,title=None,price=0):
    self.bookid=bookid
    self.title=title
    self.price=price
 def showBook(self):
   print("BookId: : ",self.bookid)
   print("Book Title : ",self.title)
   print("Book Price",self.price)



b1=Book(1,"Atomic Habbits",400)
b1.showBook()


