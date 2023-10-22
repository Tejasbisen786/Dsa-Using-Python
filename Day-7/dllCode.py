class Node:
    def __init__(self,start=None):
        self.start=start


class DLL:
    def __init__(self, prev=None,item=None,next=None):
        self.item=item
        self.next=next
     # Check Whether list is empty or not
    def is_empty(self): 
        return self.start==None
    
    def insert_at_start(self,data):
        n=Node(data)
        


