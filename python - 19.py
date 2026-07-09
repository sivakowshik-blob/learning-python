for item in "plump polling paidroid" :
    print(item)

for item in [1 , 2 , 3 , 4 , 5] :
    print(item)
    print(item)
    print(item)
print(item)  

for item in (6 , 7 , 8 , 9 , 0):
    for x in ["a" , "b" , "c"]:
        print(1 , x)

# iterables

user = {
    "name" : "skomp" , 
    "age" : 1112 , 
    "can_swim" : True
}

for item in user.items():
    print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)

for keys , values in user.items():
    print(keys , values)