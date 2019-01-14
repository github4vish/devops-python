#!/usr/bin/python
import os
import os.path

print os.system("ls -l") # Executing a shell command
print os.mkdir('devopsdir', 0750) # Create a directory named path with numeric mode m
print os.rmdir('devopsdir') # Remove (delete) the directory path 

print os.chdir('/tmp') # Move focus to a different directory
for root, dirs, files in os.walk("/tmp"):
 print root
 print dirs
 print files

for filename in os.listdir("/tmp"):
 print "This is inside /tmp", filename

a=path.getsize("/tmp/file.txt") #os.getsize() # Get the size of a file
print a

print os.getcwd() # Returns the current working directory

os.getpid() # Returns the real process ID of the current process

print os.uname() # Return information about the current operating system
print os.listdir(path) # List of the entries in the directory given by path

print os.rename(src, dst) # Rename the file or directory src to dst


#os.chmod() # Change the mode of path to the numeric mode
#os.chown() # Change the owner and group id
#os.path.exists() # Check if a path exists
#os.remove(path) # Remove (delete) the file path
#os.makedirs(path) # Recursive directory creation function
#os.removedirs(path) # Remove directories recursively


