class Rectangle:
 def __init__(self):
  self.l=int(input("length:"))
  self.b=int(input("breadth:"))
 def area(self):
  return self.l*self.b
r1=Rectangle()
r2=Rectangle()
print("area 1:",r1.area())
print("area 2:",r2.area())
if r1.area()>r2.area():
 print("rectangle i is bigger")
else:
 print("rectangle 2 is bigger")
