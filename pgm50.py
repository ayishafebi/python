from abc import*
class Polygon(ABC):
 @abstractmethod
 def area(self):
  pass
class rectangle(Polygon):
 def area(self):
  l=int(input("length:"))
  b=int(input("breadth:"))
  print("area:",l*b)
class Triangle(Polygon):
 def area(self):
  b=int(input("base:"))
  h=int(input("height:"))
  print("area:",0.5*b*h)
rectangle().area()
Triangle().area()
 
