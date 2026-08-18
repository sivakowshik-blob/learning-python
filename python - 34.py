#encapsulation
class PlayerCharacter:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')

player1 = PlayerCharacter("plumpy" , 25)
player1.speak()
print(player1.speak())
print(player1.age)
print(player1.name)

# for  dictionary type 

player2 = {"name" : "plumpy" , "age" : 25}
print(player2["name"])
print(player2["age"]) 
# instead of the dot here the '[]' s are used