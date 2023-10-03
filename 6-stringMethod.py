#capitalize
txt = "hello, and welcome to my world."
data = txt.capitalize();
print(data);

#casefold
txt = "HELLO, WORLD"
data = txt.casefold();
print(data)

#center
txt = "banana";
x = txt.center(20,'*');
print(x)

#count
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

#encode
txt = "My name is Ståle";
x = txt.encode()
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(x)

#endswith
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

#expandtabs
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#find
txt = "Hello, welcome to my world.";
x = txt.find("e");
y = txt.find("k");
print(x)
print(y)

#index
x = txt.index("e"); # if not then give error instead of return -1
print(x)

#isalnum
txt = "Company12"
x = txt.isalnum()
print(x)

#isalpha
txt = "Company"
x = txt.isalpha()
print(x); #return true or false

#isascii
txt = "Company123"
x = txt.isascii()
print(x) #return true/false

#isdecimal
txt = "1234e"
x = txt.isdecimal()
print(x)

#isdigit
txt = "1234"
x = txt.isdigit()
print(x)

#isidentifier
txt = "Demo"
x = txt.isidentifier()
print(x)

#istitle
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)


#islower
txt = "hello world! 12222"
x = txt.islower()
print(x)

#isnumeric
txt = "565543"
txt2 = "-1.5"
x = txt.isnumeric()
y = txt2.isnumeric()
print(y)

#isprintable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

#isspace
txt = " "
x = txt.isspace()
print(x)

#isupper
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

#join
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

#ljust
txt = "banana"
x = txt.ljust(20,'0')
print(x, "is my favorite fruit.")

#lower
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#lstrip
txt = "     banana     "
x = txt.lstrip() # remove space from left side
print("of all fruits", x, "is my favorite")
txt2 = ",,,,,ssaaww.....banana"
x = txt2.lstrip(',.saw') 
print("of all fruits", x, "is my favorite")

#partition
# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
txt = "I could eat bananas all day"
x = txt.partition("bananas")
y = txt.partition("apples")
print(x)
print(y)

#replace
txt = "I like bananas"
txt2 = "one one was a race horse, two two was one too."
x = txt.replace("bananas", "apples")
y = txt2.replace("one", "two",2)
print(x)
print(y)

#rfind
txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)

#rindex
txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)

#rjust
txt = "banana"
x = txt.rjust(20, "O")
print(x)

#rpartition
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

#rsplit
txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)

#rstrip
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")


#split
txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

#splitlines
#split with \n
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True) #\n included or not
print(x)

#startswith
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)

#strip
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

#swapcase
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

#title
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)

#upper
txt = "Hello my friends"
x = txt.upper()
print(x)

#zfill
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.
txt = "50"
x = txt.zfill(10)
print(x)