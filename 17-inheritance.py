#Parent Class:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname;
        self.lastname = lname;
    
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe");
x.printname();
        
#Child Class: inherit parent class Property
 # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
class Student(Person):
    def __init__(self, fname, lname):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname) # using super
        self.graduationyear = 2019
x = Student("mohit", "kapadiya")
print(x.graduationyear)
x.printname()
