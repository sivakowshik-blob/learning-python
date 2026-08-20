def multipy_by2(list):
    new_list = []
    for item in list:
        new_list.append(item * 2)
    return new_list

print(multipy_by2([1, 2, 3, 4, 5]))   
print(list(map(multipy_by2 , [1, 2, 3, 4, 5])))  