#!/usr/bin/env python3
 
import sys
import math
 
# avs 10/12/22 PFB python prob set 4 solutions
 
favs = ['crypto', 'science', 'programming', 'gf', 'dogs']
 
print(favs) # prints list
  
print(favs[2]) # prints middle element, 5 elements and index stars w/ zero
  
favs[2] = 'Foo Fighters' # replace middle position with another item, 2 again bc 0 is index start
 
print(favs)
 
favs.append('soccer') # append another item to right end of list
  
print(favs)
 
favs.insert(0,'breweries') # insert item at the beginning of the list
 
print(favs)

favs.pop() # removes last item from list

print(favs)

favs.pop(0) # removes item at index from list

print(favs)

hates = ['country music', 'stupid ppl', 'violence', 'greed'] # make new list to join

favs_hates = favs + hates # join lists

print(favs_hates)

# Write a script that splits a string into a list.

taxa = 'sapiens, erectus, neanderthalensis'

print(taxa)

print(taxa[1]) # prints second letter or index 1

print(type(taxa)) # tells the class of taxa

species = taxa.split(', ') # split the string into works and places ', ' in between them

print(species)

print(species[1]) # prints second word bc now split

print(type(species))

sort_species = sorted(species) #sort list in alphabetical order

print(sort_species)

lsort_species = sorted(species, key=len) #sort strings in list by length

print(lsort_species)

# Using the Python interpreter, interrogate the difference between these two ways to copy a list

my_list = ['a', 'bb', 'ccc']

list_copy = my_list

print(my_list)

list_copy.append('dddd')

print(list_copy)

print(my_list) # you altered the variable my_list by altering the copy, bc they are ==

my_list2 = ['a', 'bb', 'ccc']

list_copy2 = my_list2.copy()

print(my_list2)

list_copy2.append('dddd')

print(list_copy2)

print(my_list2) # does not alter OG list bc append happens only on the new copy/variable

# Write a script that uses a while loop to calculate the factorial of 1000.

num = 1000 # start from 1 and factorial of 0 = 1
n = 1000

while n >= 1: 
    num = num * n # define num as num * (n-1)!
    n = n - 1
    print('factorial at n', n, num)
print("done")

# Print out only the values that are even

numbers = [101,2,15,22,95,33,2,27,72,15,52]

evens = [evens for evens in numbers if evens%2==0]
print(evens)

sort_numbers = sorted(numbers) #sort list

for nums in sort_numbers: #print sorted nums
  print(nums)
  
odds = [odds for odds in numbers if odds%2!=0] # get odds
print(odds) 

sum_odds = sum(odds) # get the sum of numbers in a list
sum_evens = sum(evens)

print(f'''Sum of even numbers: {sum_evens}
Sum of odd numbers: {sum_odds}''')

# Write a script that uses range() in a for loop to print out every number between 0 and 99

range99 = range(0,100) #define range (0,99)

for num in range99:
    print(num)
for num in range(0,101): #modified to print 0-100
    print(num)    
    
#Create a new script that uses list comprehension to do the same thing as above

[print (item) for item in range(0,101)]

# Write a new script that takes the start and end values from the command line. If you call your script like this count.py 3 10 it will print the numbers from 3 to 10.

start = int(sys.argv[1])
end = int(sys.argv[2])

for val in range(start, end+1):
    print(val)
    
for val in range(start, end+1):
    if val % 2!=0:
        print(val)
        
# Write a new script to create a list with the following data ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']. 

dna = ['ATGCCCGGCCCGGC', 'GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT', 'ATGGGCCC']

for nt in dna:
    print(nt)
    
for nt in dna:
    print(len(nt),'/t',nt)
    
dna_tup = [(len(nt),nt) for nt in dna]

for index in range(len(dna)):
    print(index + 1, len(dna[index]), dna[index],sep='t')
