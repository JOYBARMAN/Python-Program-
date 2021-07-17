my_set=set()
my_set.add(2)
my_set.add(6)
my_set.add((1,2,3,4,5)) # we cannot add a dictionary or a list in the set but we add tuple in the set
# my_set.add({1:2})
print(my_set)

# romove element from the set
my_set.remove(2)
print(my_set)
print('-'*50)
my_set.pop()
print(my_set)