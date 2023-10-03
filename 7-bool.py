#bool boolean

print("*******************************  Print boolean  ******************************************");
print(bool("Hello")) #True
print(bool(15)) #True

print("*******************************  False Values  ******************************************");
#False Values
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print("*******************************  isinstance  ******************************************");
#isinstance : Check instance of it's specific types
x = True
print(isinstance(x, bool))

print("*******************************  Logical Operators and/or/not  ******************************************");
#Logical Operators and/or/not
x = 10; 
print(x>10 and x<20);
print(x>10 or x<20);
print(not(x>10 or x<20));

print("*******************************  Identity Operators is/ is not  ******************************************");
#Identity Operators is/ is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x is not z)

print("*******************************  Membership Operators in/ not in  ******************************************");
#Membership Operators in/ not in
x = ["apple", "banana"]
print("banana" in x)
print("banana" not in x)

