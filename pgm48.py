class Bank:
 def __init__(self):
  self.name=input("enter name:")
  self.b=int(input("enter balance:"))
 def deposit(self):
  self.b+=int(input("deposit:"))
 def withdraw(self):
  a=int(input("withdraw:"))
  if a<=self.b:
   self.b-=a
  else:
   print("insufficient balance")
 def display(self):
  print(self.name,self.b)
x=Bank()
x.deposit()
x.withdraw()
x.display()
  
