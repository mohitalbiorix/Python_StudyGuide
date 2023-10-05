""" The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

 """

#try / except
try:
    print(x)
except:
    print("An exception occurred")
    
# many except
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
#try / except / else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#try / except / else / finally 
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")



#user Input # Python 2.7 uses the raw_input() method.
username = input("Enter user name:");
print("username is:" +username )