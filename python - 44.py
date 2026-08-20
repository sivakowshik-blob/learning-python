my_list = [1 , 2 , 3 , 4 , 5]
your_list = [10 , 20 , 30 , 40 , 50]
their_list = [100 , 200 , 300 , 400 , 500]
def multipy_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd , my_list)))
print(list(map(multipy_by2 , my_list)))
print(list(zip(your_list , my_list , their_list)))
print(my_list)