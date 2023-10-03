
#List

""" 
Lists are used to store multiple items in a single variable.
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc. 
"""

#list
list = ["apple", "banana", "cherry", "apple"]

print("*******************************  Print List  ******************************************");
print(list) # print list
print(len(list)) # length of list
print(type(list)) # type of list always list

print("*******************************  List Constructor  ******************************************");
#list constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

print("*******************************  Access list item  ******************************************");
#access list item
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[1])
print(list[-1]) #start from the end
print(list[2:5]) #range
print(list[2:])
print(list[:4])
print(list[:-4]) #['apple', 'banana', 'cherry']
print(list[-4:-2]) #['orange', 'kiwi']

print("*******************************  Change list item  ******************************************");
#change list item
list = ["apple", "banana", "cherry"]
list[1] = "blackcurrant"
print(list)

#Change a Range of Item Values
list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list[1:3] = ["blackcurrant", "watermelon"]
print(list)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
list = ['apple','banana','cherry'];
list[1:2] = ["blackcurrant", "watermelon"];
print(list) # chnage banana to "blackcurrant", "watermelon"

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
list = ["apple", "banana", "cherry"]
list[1:3] = ["watermelon"] # change banana and cherry to watermelon
print(list)

print("*******************************  Add list item  ******************************************");

list = ["apple", "banana", "cherry"]

#append item : added item end of the list
list.append('guava');
print(list);

#insert: added item at a specefic index
list.insert(2, "mango");
print(list)

#extend list: To append elements from another list to the current list
list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list1.extend(list2)
print(list1);

#we can extend tuple into list also
list = ["apple", "banana", "cherry"]
tuple = ("kiwi", "orange")
list.extend(tuple);
print(list)

print("*******************************  Remove list item  ******************************************");

#remove : remove specific item
list = ["apple", "banana", "cherry","banana"]
list.remove("banana")
print(list)

#pop: remove from sepcific index
list = ['apple', 'banana', 'cherry'];
list.pop(); #last remove
list.pop(1) # remove from given specific index
print(list)

#del : remove from specific index
list1 = ['apple', 'banana', 'cherry'];
del list1[0];  # delete item from 0 index
#del list1 # delete completely list , ref also delete
print(list1)

#clear : empties the list. The list still remains, but it has no content.
list = ['apple', 'banana', 'cherry'];
list.clear();
print(list) #[]

print("*******************************  Loop in list  ******************************************");

list = ["apple", "banana", "cherry"];

#for loop
for x in list:
    print(x)
print(" \n")

for i in range(len(list)):
    print(list[i])
print(" \n")

#while loop
i = 0;
while i < len(list):
    print(list[i]);
    i=i+1;
print(" \n")

