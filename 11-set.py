#Set

"""
    Sets are used to store multiple items in a single variable.
    A set is a collection which is unordered, unchangeable*, and unindexed.
"""

print("*******************************  Print Set  ******************************************");

thisset = {"apple", "banana", "cherry"}
print(thisset)

print("*******************************  Duplicates Not Allowed  ******************************************");

thisset = {"apple", "banana", "cherry", True,1,2}
print(thisset) # True,1 consider same 

print("*******************************  Type Set  ******************************************");

myset = {"apple", "banana", "cherry"}
print(type(myset))

print("*******************************  Constructor Set  ******************************************");

thisset = set(("apple", "banana", "cherry"));
print(thisset);

print("*******************************  Access Set  ******************************************");
thisset = set(("apple", "banana", "cherry"));
for x in thisset:
    print(x)

print("*******************************  Add Set Item  ******************************************");

#add set item
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset);

#update(): To add items from another set into the current set
set1 = {1,2,3};
set2 = {4,5,6};
set1.update(set2);
print(set1);

#upadte() with list
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"];
thisset.update(mylist);
print(thisset);

print("*******************************  Remove Set Item  ******************************************");

#remove()
 #If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana");
# thisset.remove("guava") #raised error
print(thisset)

#discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
thisset.discard("guava") # Not raised error
print(thisset)

#pop() : remove from last
thisset = {"apple", "banana", "cherry"}
thisset.pop();
print(thisset)

#clear(): clear set
thisset = {"apple", "banana", "cherry"}
thisset.clear();
print(thisset);

#del: delete set completely
thisset = {"apple", "banana", "cherry"};
del thisset;
# print(thisset) #raised error


print("*******************************  Join Set Item  ******************************************");
#Join set

#union(): returns a new set containing all items from both sets
set1 = {"a","b","c"};
set2 = {1,2,3,"c"};

set3 = set1.union(set2);
print(set3)

#update(): method that inserts all the items from one set into another:
set1 = {"a","b","c"};
set2 = {1,2,3};

set1.update(set2);
print(set1)

print("*******************************  Keep ONLY the Duplicates  ******************************************");

# intersection_update() : keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"};
y = {"google", "microsoft", "apple"};
x.intersection_update(y);
print(x)#{apple}

# intersection() : return a new set,keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"};
y = {"google", "microsoft", "apple"};
z = x.intersection(y);
print(z) #{apple}

print("*******************************  Not Keep the Duplicates  ******************************************");

x = {"apple", "banana", "cherry"};
y = {"google", "microsoft", "apple"};
x.symmetric_difference_update(y);
print(x) #{'banana', 'microsoft', 'google', 'cherry'}

x = {"apple", "banana", "cherry"};
y = {"google", "microsoft", "apple"};
z= x.symmetric_difference(y);
print(z) #{'banana', 'microsoft', 'google', 'cherry'}

