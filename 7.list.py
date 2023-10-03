
thislist = ["apple", "banana", "cherry"]
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# access item
print(thislist[1])
print(thislist[-2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# change list item
thislist[1] = "pokpok"
print(thislist)

# add list item
thislist.append("naina")
print(thislist)

# add by index
thislist.insert(6, "kiki")
print(thislist)

# remove list 
thislist.remove("cherry")
print(thislist)

# loop list 
for x in thislist:
  print( x)


# list compreshension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print ("array appended: " , newlist)


# copy list
mylist = thislist.copy()
print("list copy: " , mylist)

# join list 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
