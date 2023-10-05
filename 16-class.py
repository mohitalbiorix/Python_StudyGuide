
#__init__ ()
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# The __init__() function is called automatically every time the class is being used to create a new object.

print("******************************* __init__() ********************************************");
class Person:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
p1 = Person("John", 36);
print(p1); #return obj
print(p1.name , p1.age);


print("******************************* __str__() ********************************************");
#__str__()
# The __str__() function controls what should be returned when the class object is represented as a string.
# The __str__() function controls what should be returned when the class object is represented as a string.

class Person:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
    
    def __str__(self):
        return f"{self.name},{self.age}"
        
    def myfun(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36);
print(p1);
p1.myfun();

print("******************************* self parameter ********************************************");

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Student:
    def __init__(self,name,age):
        self.name = name;
        self.age= age;
    
    def myfun(self):
        print("Hello my name is " +self.name+ "and My age is "+ str(self.age));
s1 = Student("Mohit", 24);
s1.age = 25; # can modify object property.
s1.myfun();

print("******************************* pass statement ********************************************");
class Person:
  pass