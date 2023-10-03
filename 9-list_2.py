print("*******************************  List Comprehension  ******************************************");
# List Comprehension
""" 
    List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

    Syntax:
    newlist = [expression for item in iterable if condition == True]   

 """
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newList1 = [x for x in fruits];
newList2 = [x for x in fruits if x != 'banana'];
newList3 = [x.upper() for x in fruits];
newlist4 = ['hello' for x in fruits];
newlist5 = [x if x != "banana" else "orange" for x in fruits]
print(newList1);
print(newList2);
print(newList3);
print(newlist4);
print(newlist5)

numList = [x for x in range(10) if x<5];
print(numList)

print("*******************************  Sort List  ******************************************");

#sort
list = ["orange", "mango", "kiwi", "pineapple", "banana"];
list.sort()
print(list)

list = [100, 50, 65, 82, 23]
list.sort();
print(list)

#decending order
list.sort(reverse=True);
print(list)

#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case
list = ["banana", "Orange", "Kiwi", "cherry"];
list.sort();
print(list)

#convert all into lower befor sort
list.sort(key = str.lower);
print(list);

#reverse order sort
list =  ["banana", "Orange", "Kiwi", "cherry"];
list2 = [10,30,2,45,3];
list.reverse();
list2.reverse();
print(list);
print(list2);


print("*******************************  Copy List  ******************************************");

""" 
    You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2. 
"""

list1 = ["apple", "banana", "cherry"];
list2 = [1,2,3];

# list2 = list1

# list2[0] = 1;
# print(list2); #[1, 'banana', 'cherry']
# print(list1); #[1, 'banana', 'cherry']

#copy
list2 = list1.copy();
print(list2)
list2[0] = 1;
print(list1) #['apple', 'banana', 'cherry']
print(list2) #[1, 'banana', 'cherry']

#list() 
list1 = ['apple', 'banana', 'cherry'];
list2 = list(list1);
list2[0] = 1;
print(list1);
print(list2);

print("*******************************  Join List  ******************************************");

# using + operator
list1 = ['apple', 'banana', 'cherry'];
list2 = [1,2,3]
list3 = list1 + list2;
print(list3)

# using for loop
for x in list2:
    list1.append(x);
print(list1)

# extend
list1.extend(list2);
print(list1)

#count
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

#join list
fruits = ["apple", "banana"]
list = fruits * 2;
print(list); #["apple", "banana","apple", "banana"]
