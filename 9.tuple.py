thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# access tuple
print(thistuple[1])

# update tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# unpack tuple
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# loop tuple
for i in range(len(thistuple)):
  print(thistuple[i])

# count method
thistuple1 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple1.count(5)
print(x)