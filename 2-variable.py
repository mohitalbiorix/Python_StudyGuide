
""" variables

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords. 

"""

print("******************************* Create Variables ******************************************");
x = 5;  #int data type
name = "Mohit"; #str data type

print(x);
print(name);

print("******************************* Type Casting ******************************************");
#casting
#convert one data type to another data type

y = str(x); #convert int to str
z = float(x); #convert int to float

print(y);
print(z);

print("******************************* Get types of varibale ******************************************");
#Get type

a = type(x); #return typeof x
b = type(y); #return typeof y
c = type(z); #return typeof z

print(a);
print(b);
print(c);

print("******************************* Assign multiple values to multiple variables ******************************************");
# Assign multiple values to multiple variables

x, y, z = "Orange", "Banana", "Cherry"
print(x);
print(y);
print(z);

print("*******************************  Assign one value to multiple variables ******************************************");
# Assign one value to multiple variables

x=y=z="Banana";
print(x);
print(y);
print(z);

print("*******************************  Unpack collection ******************************************");
# Unpack collection

fruits = ["Orange", "Banana", "Cherry"];
x,y,z = fruits;
print(x);
print(y);
print(z);

print("*******************************  Output a variable ******************************************");

# output multiple variables, separated by a comma:
x = "John "
y = "Dev"
print(x, y)
print(x + y)

print("*******************************  Create global variable ******************************************");

# Here, x is global variable
x = "awesome";

def myfunc():
  print("Python is " + x)

myfunc()

#Using global keyword

globalStr = "globalStr"
def globalFun():
  global globalStr 
  globalStr = "This is global";
  print(globalStr);

globalFun()
print(globalStr)