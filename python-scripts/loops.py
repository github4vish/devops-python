#!/usr/bin/python
print "*********while loop******************"
count = 0
while (count < 12):
 print 'The count is:', count
 count = count + 1
print "Good bye!"

print "*********for loop******************"
for word in 'DevOps!':
# First Example
 print 'Current Word :', word
planets = ['Mercury', 'Venus','Earth']
for planet in planets:
# Second Example
 print 'Current planet :', planet
print "Bye!"

print "*********range in loop******************"
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
 print 'Current fruit :', fruits[index]
print "Good bye!"

print "*********break in loop******************"
for word in 'Python':
# First Example
 if word == 't':
  break
 print 'Current Letter :', word
a = 10
# Second Example
while a > 0:
 print 'Current variable value :', a
 a = a -1
 if a == 5:
  break
print "Execution completed!"


print "*********continue in loop******************"
for word in 'Python':
# First Example
 if word == 't':
  continue
 print 'Current Letter :', word
a = 10
# Second Example
while a > 0:
 a = a -1
 if a == 5:
  continue
 print 'Current variable value :', a
print "Execution completed!"
