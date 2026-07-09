#sets
my_set1 = {1 , 2 , 3 , 4 , 5}
print(my_set1)
my_set2 = {1 , 2 , 3 , 4 , 5 , 5}
print(my_set2)
my_set1.add(100)
my_set1.add(2)
print(my_set1)
new_set = my_set2.copy
my_set1.clear()
print(my_set1)
print(new_set)

my_set3 = {1 , 2 , 3 , 4 , 5}
your_set = {4 , 5 , 6 , 7 , 8 , 9 , 10}
print(my_set3.difference(your_set))
print(my_set3.discard(5))
print(my_set3.intersection(your_set))


my_set4 = {1 , 2 , 3 , 4 , 5}
print(my_set4.difference_update(your_set))
print(my_set4)
print(my_set4.isdisjoint(your_set))
print(my_set4.union(your_set)) #instead of using the union() we can also use | symbol

my_set5 = {4 , 5}
print(my_set5.issubset(your_set))
print(my_set5.issuperset(your_set))
print(your_set.issuperset(my_set5))