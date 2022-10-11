#!/usr/bin/env python3
import sys

#print name
name = 'Alex'
print('My name is:',name)

#print favorite color
color = 'Blue'
print('My favorite color:',color)

#print favorite activity
activity = 'Coding'
print('My favorite activity:',activity)

#print favorite animal
animal = 'Dogs'
print('My favorite animal:',animal)

#print individual via sys.argv
name1 = sys.argv[1]
color1 = sys.argv[2]
activity1 = sys.argv[3]
animal1 = sys.argv[4]
print('My name:',name1,'\nMy favorite color: ',color1,'\nMy favorite activity:',activity1,'\nMy favorite animal:',animal1)

