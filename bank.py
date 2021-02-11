class bank():
    def __init__(self,acnt,num,typ,amt):
        self.ac=acnt
        self.name=num
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("acnt name",self.name)
        print("Acnt num=",self.ac)
        print("bal=",self.amount)
    def with1(self,w1):
        return(self.amount-w1)
n=input("enter name ")
t=input("enter type ")


a=int(input("enter numbr: "))
am=int(input("enter amnt "))
obj=bank(a,n,t,am)
print("account details")
obj.printamt()
w=int(input("enter amt to withdraw "))
print("b1=",obj.with1(w))


#print()
