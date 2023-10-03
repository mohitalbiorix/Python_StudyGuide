a = 332
b = 200
if b > a:
    print("b is grater than a")
elif a == b:
    print("b is equalto a")
else:
    print("a is grater than b")
    
#short hand: If you have only one statement to execute
if a > b: print("a is greater than b")

#Short Hand If ... Else
print("A") if a > b else print("B")

#multiple short hand else if statement
print("A") if a > b else print("=") if a == b else print("B")

#and 
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
#or
if a > b or c > a:
  print("Both conditions are True")
  
#not
if not a > b:
  print("a is NOT greater than b")
  
#pass statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

