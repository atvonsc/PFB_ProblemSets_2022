#!/usr/local/bin/python3

import sys
import math

#avs 10/14/22 python prb set 5 solutions

#Write a script in which you construct a dictionary of your favorite things.
favs_dict = {'Book': 'To Kill a Mockingbird',
						 'Song': 'Learn to fly',
						 'Tree': 'Aspen'}

print(favs_dict['Book']) #print out fav book

fav_book = 'Book' #print gav book as variable

print(favs_dict[fav_book])

print(favs_dict['Tree']) #print fav tree

fav_organism = 'Organism' #add fav organism to the dict

favs_dict[fav_organism] = 'Homo sapiens'

print(favs_dict['Organism'])

favs_dict_keys = ', '.join(list(favs_dict.keys())) #print out all the keys
# to the user so that they know what to pick from.

fav = input('Add the type of your favorite thing (' + favs_dict_keys + '):')
print(favs_dict[fav])

favs_dict['Organism'] = 'E. coli' # change value of organism

# Get the fav_thing from the command line and a new value for that key. Change the value with the user inputted value.

add_fav_key = input('Add a new category of favorite thing: ')
add_fav_thing = input('Add your favorite thing to this new category: ')

favs_dict[add_fav_key] = add_fav_thing

# Use a for loop to print out each key and value of the dictionary

for k, v in favs_dict.items():
  print(k, v, sep = '\t')

print('Lesson finished')
