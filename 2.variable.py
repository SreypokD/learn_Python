
# variable name 
my_var = "pokpok"


# var muliple value
# ex1============
name, age, gender = "pokpok" ,"20" , "lady"
# print(name, age, gender )

# ex2============
x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# ex3 ===========
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
# print(x)
# print(y)
# print(z)

# Global variable 
# === outsite====
x = "poki"
def myfunc():
  print("Python is " + x)

myfunc()

# ==insite=====
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)