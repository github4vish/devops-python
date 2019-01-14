#!/usr/bin/python
print "**************normal varibles **********************"
mynumber = 86 # A integer variable assignment
myfloatnumber = 86. 11 # A float variable assignment
myname = “imran” # A string variable assignment

print mynumber
print myfloatnumber
print myname


print "**************string varibles **********************"
teststr = 'Hello DevOps!'
print teststr # Prints complete string
print teststr[0] # Prints first character of the string
print teststr[0:5] # Prints characters starting from 0th to 5 th
print teststr[6:12] # Prints characters starting from 6th to 12th
print teststr[3:] # Prints string starting from 3rd character
print teststr * 2 # Prints string two times
print teststr + " Hola" # Prints concatenated string

print "**************list varibles **********************"
list1 = [ 'ansible', 1111 , 'puppet', 86.96, 'git', 'aws']
list2 = ['miner', 'boy']
print list1 # Prints complete list
print list1[0] # Prints first element of the list
print list1[-1] # Prints last element of the list
print list1[2:4] # Prints elements starting from 2nd till 4th
print list1[3:] # Prints elements starting from 3rd element
print list2 * 2 # Prints list two times

print "**************tuple varibles **********************"
tuple1 = ( 'ansible', 1111, 'puppet', 86.96, 'git', 'aws')
tuple2 = ('miner', 'boy')
print tuple1 # Prints complete list
print tuple1[0] # Prints first element of the list
print tuple1[1:3] # Prints elements starting from 2nd till 3rd
print tuple1[2:] # Prints elements starting from 3rd element
print tuple2 * 2 # Prints list two times
print tuple1 + tuple2 # Prints concatenated lists

print "**************list vs tuple varibles **********************"
tuple = ('ansible', 1111, 'puppet', 86.96, 'git', 'aws'
list = ['ansible', 1111, 'puppet', 86.96, 'git', 'aws']
tuple[5] = ‘terra’ # Invalid syntax with tuple
list[5] = ‘terra’ # Valid syntax with list

print "**************dictionary varibles **********************"
dict1 = {}
dict1['profile'] = "hitman"
dict1['passcode'] = "zeus"
dict2 = {'name': 'imran','code':47, 'dept': 'hitman'}
print dict1['profile'] # Prints value for 'profile' key
print dict1['passcode'] # Prints value for 'passcode' key
print dict2 # Prints complete dictionary
print dict2.keys() # Prints all the keys
print dict2.values() # Prints all the values



print "**************comparitive operators **********************"
a = 2
b = 30
if ( a == b ):
 print "a is equal to b"
else:
 print "a is not equal to b"
if ( a != b ):
 print "a is not equal to b"
else:
 print "a is equal to b"
if ( a < b ):
 print "a is less than b"
else:
 print "a is not less than b"
if ( a > b ):
 print "a is greater than b"
else:
 print "a is not greater than b"

print "**************membership operators **********************"
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
if ( a in list ):
 print "a is available in the given list"
else:
 print "a is not available in the given list"
if ( b not in list ):
 print "b is not available in the given list"
else:
 print "b is available in the given list"
a = 2
if ( a in list ):
 print "a is available in the given list"
else:
 print "a is noi available in the given list"

