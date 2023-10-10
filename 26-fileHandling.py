""" File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

 """

#open()
#takes two parameters; filename and mode

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists 
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

f = open('demofile.txt');
print(f); # <open file 'demofile.txt', mode 'r' at 0x00000000027010C0>

print("******************************* Read Files******************************************")

#read()
print(f.read());
print(f.read(5)); #return first 5 char.

#readline(): We can read only first line
#By calling readline() two times, you can read the two first lines:
print(f.readline())
print(f.readline())

#Read file by looping
f = open("demofile.txt", "r")
for x in f:
    print(x , "by loop")

#close file
#It is a good practice to always close the file when you are done with it.
f.close();

print("******************************* Write/Create Files ******************************************")
#w : overwrite all content
#a : add content last into  file
#x : create new file, error if exist
f = open("demofile2.txt", "w");
f.write("Now the file has more content!");

# f = open("myfile.txt","x");

print("******************************* Delete File ******************************************")
# need to import os module

import os;

os.remove('demofile2.txt') # for delete file
os.rmdir("myfolder") #remove folder

