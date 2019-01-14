#! /usr/bin/python

print "*******String Functions******* "
str = "this is string example....wow!!!";
print "str.capitalize() : ", str.capitalize()

str1 = "this is string example....wow!!!";
str2 = "exam";
print str1.find(str2);
print str1.find(str2, 10);
print str1.find(str2, 40);

str = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print str.join( seq );

a = "Hello    "
a.rstrip()

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );

aList = [123, 'xyz', 'zara', 'abc'];
aList.append( 2009 );
print "Updated List : ", aList;

aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print "Extended List : ", aList ;

aList = [123, 'xyz', 'zara', 'abc']
aList.insert( 3, 2009)
print "Final List : ", aList

aList = [123, 'xyz', 'zara', 'abc'];
print "A List : ", aList.pop();
print "B List : ", aList.pop(2);


print "Dictionary functions"
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
del dict['Name']; # remove entry with key 'Name'
dict.clear(); # remove all entries in dict
del dict ; # delete entire dictionary
print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];
