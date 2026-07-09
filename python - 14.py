#dictionary
dictionary = {
    "a" : [1 , 2 , 3],
    "b" : "hello",
    "x" : True
} 
my_list = [
    {
    "a" : [1 , 2 , 3],
    "b" : "hello",
    "x" : True
    },
    {
    "a" : [4 , 5 , 6],
    "b" : "hello",
    "x" : True
    }
]
print(my_list[0]["a"][2])
print(dictionary["a"][1])

user1 = {
    "basket" : [1 , 2 , 3],
    "greet" : "hello"
}
print(user1.get("age"))
print(user1.get("age" , 55))
user2 = {
    "basket" : [1 , 2 , 3],
    "greet" : "hello", 
    "age" : 20
    }
print(user2.get("age" , 55))

user3 = dict(name = "PulkyPulky")
print(user3)

print("basket" in user2)
print("size" in user2)
print("age" in user2.keys())
print(user2.items())
print(user2.clear)
user3.clear
print(user3)
user4 = user1.copy 
print(user4)
print(user1.pop("age" , 55))
print(user1)
print(user2.update({"age" : 32}))
print(user3)
print(user3.update({"age" : 45}))
print(user3)