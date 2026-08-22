# dictionary comprehension
simple_dict = {
    "a": 1,
    "b": 2,
}
my_dict = {k:v**2 for k,v in simple_dict.items()}
my_dict = {k:v**2 for k,v in simple_dict.items() if v%2 == 0}
my_dict2 = {num:num**2 for num in [1,2,3,4,5]}

print(my_dict2)