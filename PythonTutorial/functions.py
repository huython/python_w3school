def my_function():
  print("hello from a function")

my_function()

def my_function2(fname):
  print(fname + " Refsnes")

my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")

def my_function3(country = "Vietnam"):
  print("I am from " + country)

my_function3("Thailand")
my_function3("India")
my_function3()
my_function3("US")

def my_function4(x):
  return 5 * x

print(my_function4(3))
print(my_function4(5))
print(my_function4(9))