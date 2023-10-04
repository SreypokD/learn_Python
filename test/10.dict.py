thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# access item
thisdict.update({"color": "red"})

# loop dict
for x in thisdict:
  print("value item: ", thisdict[x])

#value()===================
for x in thisdict.values():
  print("value: " ,x)
# key()=====================
for x in thisdict.keys():
  print("keys : ",x)
#item()===================== 
for x, y in thisdict.items():
  print("keys:" ,x ," and ","values:", y)

# copy dict
mydict = dict(thisdict)
print(mydict)

# nested dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


print(myfamily["child2"]["name"])






















# remove  item 
thisdict.pop("model") #spacific item remove
thisdict.popitem()    #last index
thisdict.clear()      #clear all item