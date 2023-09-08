#!/usr/bin/python3

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)

#  return no of times apple appears in list
print(fruits.count('apple')) 

# use index to find item index 
print(fruits.index('banana'))

# Find next banana starting at position 4
print(fruits.index('banana', 4))

# reverse list
fruits.reverse()
print(fruits)

#  add items to list
fruits.append('grape')
print(fruits)

#  use `sort` to rearrange the list - usually in ascending/alphabetical order
fruits.sort()
print(fruits)

# use pop to single out item - using the index number or just empty paranthesis to return last item
print(fruits.pop())
print(fruits)
print(fruits.pop(4))
print(fruits)
#  use insert
fruits.insert(4, 'coconut')
print(fruits)
