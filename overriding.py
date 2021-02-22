class  publisher:
    def __init__(self,pname):
       self.pname=pname
       def display(self):
           print("name",self.pname)
class book(publisher):
    def __init(self,pname,bname,title):
     self.pname=pname
     self.bname=bname
     self.title=title
    def display(self):
       print("pname",self.name)
       print("bname",self.bname)
       print("title",self.title)
       
class python(book):
    def __init__(self,pname,bname,title,page,price):
     self.pname=pname
     self.bname=bname
     self.title=title
     self.page=page
     self.price=price
    def display(self):
      print("pname",self.pname)
      print("book",self.bname)
      print("title",self.title)
      print("pages",self.page)
      print("prie",self.price)
n=input("enter publisher")
b=input("enter book")
t=input("enter title")
p=int(input("enter pages"))
pr=int(input("enter price"))
obj=python(n,b,t,p,pr)
obj.display()

    
