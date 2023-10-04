def my_function():
  print("Hello from a function")
my_function()

# pass argument==========================================
def my_func(name):
  print(name + " is cutes.")
my_func("dd")

#pass list ==============================================
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# return values =========================================
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# function with two arguments============================
def mityply(num1 , num2):
  multy = num1 * num2
  return multy

resutl = mityply(2,3)
print(resutl)

# Library Function=======================================
import math
# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power 
power = pow(2, 3)
print("2 to the power 3 is",power)



