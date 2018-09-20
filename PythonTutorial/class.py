class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Huy", 32)
print(p1.name, p1.age)
p1.myfunc()

p1.age = 40
print(p1.name, p1.age)

del p1.age
#print(p1.name, p1.age)

del p1
#print(p1.name, p1.age)