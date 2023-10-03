#dictionary

""" 
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name. 

"""

#dictionary example

print("******************************* Print dictionary  ******************************************");
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(thisdict['brand']) # Ford
print(len(thisdict)) # length of dict

print("******************************* Type of  dictionary  ******************************************");
print(type(thisdict))

print("******************************* Dictionary constructor  ******************************************");
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict);

print("******************************* Access dictionary  ******************************************");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#get item
x = thisdict['year'];
print(x)

#access item using get method
x= thisdict.get('year');
print(x);

#get all keys
keys = thisdict.keys();
print(keys);

#add key
thisdict['color'] = 'white';
print(thisdict)

#get values
values = thisdict.values();
print(values);

#items() : The items() method will return each item in a dictionary, as tuples in a list.


print("******************************* Change Dictionary Items  ******************************************");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#direct chnages on key
thisdict['year'] = 2018; #if item does not exits, item will be added
print(thisdict);

#using update methods
#The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
#if item does not exits, item will be added
thisdict.update({"year": 2020})
print(thisdict);

print("******************************* Remove Dictionary Items  ******************************************");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#pop: removes the item with the specified key
thisdict.pop("year");
print(thisdict);

#popitem: removes the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem();
print(thisdict);

#del: removes the item with the specified key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#del keyword can also delete the dictionary completely
# del thisdict

#clear: empties the dictionary:
# thisdict.clear()

print("******************************* Loop Through a Dictionary  ******************************************");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#for loop
for x in thisdict:
  print(x)
print('************************')
 
#print all values
for x in thisdict:
  print(thisdict[x])
print('************************')
  
#loop of values
for x in thisdict.values():
  print(x)
print('************************')

#both key and value print
for x, y in thisdict.items():
  print(x, y)

print("******************************* Copy of dictionary  ******************************************");

#copy of dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict.copy()
print(mydict);

#using dict method
mydict = dict(thisdict);
print(mydict);

print("******************************* Nested dictionary  ******************************************");

#nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily);
print(myfamily['child1']['name'])

print("******************************* dictionary methods  ******************************************");

#fromkey(): returns a dictionary with the specified keys and the specified value
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x,y);
print(thisdict)

#setdefault(): returns the value of the item with the specified key.If the key does not exist, insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(car)