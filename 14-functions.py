#function
def my_fun():
    print("Hello from a function");

my_fun()

#pass function arguments
def my_fun(fname, lname):
    print(fname+" "+lname);

my_fun("Mohit", "Kapadiya");

#*args: If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition
def my_fun(*args):
    print(args);
my_fun("Mohit", "Kapadiya");

#pass with keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#**kwargs: If you do not know how many keyword arguments that will be passed into your function
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#pass statement :function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass

