""" Strings in python are surrounded by either single quotation marks, or double quotation marks. """

print("*******************************  Single line string ******************************************");
# Single line string
x = "Mohit";
print(x);

print("*******************************  Multiline string ******************************************");
# Multiline string
a = """Lorem ipsum dolor sit amet   ,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a);

#other way print multiline string
a = '''Lorem ipsum dolor sit amet   ,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a);

print("*******************************  Length of string ******************************************");

# len() function

a = "Mohit Kapadiya";
print(len(a));

print("*******************************  Check string ******************************************");

txt = "The best things in life are free!";

print("best" in txt);
print("best" not in txt);

print("*******************************  Slicing ******************************************");

b = "Hello, World!";
print(b[2:5]);
print(b[:5]);
print(b[5:]);

print("*******************************   Modify Strings  ******************************************");

a = "Hello, World!"
b = "HELLO WORLD!"
c = "  hello world!  "
d = "HELLO WORLD!"

print(a.upper()); # upper case 
print(b.lower()); # lower case
print(c.strip()); # remove whitespace
print(d.replace("H", "J")); # replace H to J
print(a.split(',')) # return a list where the text between the specified separator becomes the list items

print("*******************************   Strings Format  ******************************************");

# format()

age = 36;
quantity = 3;
itemno = 567;
price = 49.95;
txt = "My name is John, and I am {}";
myorder = "I want {} pieces of item {} for {} dollars."
myorder1 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(txt.format(age));
print(myorder.format(quantity,itemno,price));
print(myorder1.format(quantity,itemno,price));