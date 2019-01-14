#!/usr/bin/python
print  "***************function***************"
def print_func( var1 ):
#This prints a passed string into this function
 print var1
 return
# Calling print_func
print_func("Testing function calling.")
# Printing & Calling print_func
print print_func("Testing function calling.")
# Storing print_func returned value
returnedvalue =print_func("Testing function calling.")
print returnedvalue

"""print  "*************** required arguments function***************"
# Function definition is here
def printme( str ):
#This prints a passed string into this function
 print str;
 return;
# Now you can call printme function
printme();"""


print  "***************keyword arguments function***************"
# Function definition is here
def printme( str ):
#This prints a passed string into this function
 print str;
 return;
# Now you can call printme function
printme( str = "My string");



# Function definition is here
def printinfo( name, age ):
#This prints a passed info into this function
 print "Name: ", name;
 print "Age ", age;
 return;
#Now you can call printinfo function
printinfo( age=50, name="miki" );

print  "***************default argument function***************"
# Function definition is here
def printinfo( name, age = 35 ):
#This prints a passed info into this function
 print "Name: ", name;
 print "Age ", age;
 return;
# Now you can call printinfo function
printinfo( age=50, name="miki" );
printinfo( name="miki" );

print  "***************varible length arguments function***************"
# Function definition is here
def printinfo( arg1, *vartuple ):
#This prints a variable passed arguments
 print "Output is: "
 print arg1
 for var in vartuple:
  print var
 return;
# Now you can call printinfo function
printinfo( 10 );
printinfo( 70, 60, 50 );

print  "***************return function***************"
# Function definition is here
def sum( arg1, arg2 ):
# Add both the parameters and return them."
 total = arg1 + arg2
 print "Inside the function : ", total
 return total;
# Now you can call sum function
total = sum( 10, 20 );
print "Outside the function : ", total
