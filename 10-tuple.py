#Tuple

""" 
    Tuples are used to store multiple items in a single variable.
    Tuple items are ordered, unchangeable, and allow duplicate values. 
"""

print("*******************************  Print Tuple  ******************************************");
#print tuple
printtuple = ("apple", "banana", "cherry", "apple", "cherry")
print(printtuple);
print(len(printtuple)) #length of tuple

print("*******************************  Type Tuple  ******************************************");
#tuple type
tupleType = ('apple');
print(type(tupleType)) #Not a tuple, str

tupleType2 =('apple',);
print(type(tupleType2)) #tuple

print("*******************************  Constructor Tuple  ******************************************");
# using tuple constructor
tuple2 = tuple(("apple", "banana", "cherry", "apple", "cherry"))
print(tuple2)

print("*******************************  Access Tuple  ******************************************");
#access tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1]);
print(thistuple[-1]);
print(thistuple[2:5]);
print(thistuple[:4]);
print(thistuple[2:]);


print("*******************************  Update Tuples  ******************************************");

# Tuple is immutable so we can't change it, but some tricky methode to channge it.
# Convert tuple to list and change it.
x = ("apple", "banana", "cherry");
y = list(x);
print(y);
y[0] = 'mango';
y.append('guava')
x = tuple(y);
print(x);

print("*******************************  Add Tuples  ******************************************");

# convert tuple to list and apply append() method
x = ("apple", "banana", "cherry");
y = list(x);
print(y);
y.append('guava')
x = tuple(y);
print(x);


# add tuple to tuple
thistuple = ('apple', 'banana', 'cherry');
y = ("orange",);
thistuple += y
print(thistuple);


print("*******************************  Unpacking  Tuples  ******************************************");

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green) #apple
print(tropic) #["mango", "papaya", "pineapple"]
print(red) #cherry

#join tuple
fruits = ("apple", "banana")
tuple = fruits * 2;
print(tuple); #("apple", "banana","apple", "banana")

#count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x= thistuple.count(5);
print(x) #2

#index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x) #3