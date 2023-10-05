""" 
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__(). 

"""

#iter() in tuple
mytuple = ("apple", "banana", "cherry");
myit = iter(mytuple);

#next()
print(next(myit))
print(next(myit))
print(next(myit))

#string are also iterable 
fruit = "banana";
myit = iter(fruit);

#next()
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Create an Iterator using class
class MyNumber:
    def __iter__(self):
        self.a=1;
        return self;
    
    def __next__(self):
        x = self.a;
        self.a += 1;
        return x;
myClass = MyNumber();
myiter = iter(myClass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
