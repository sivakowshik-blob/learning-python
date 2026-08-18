class PlayerCharacter:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def run(self):
        print("run")
        return "done"

player1 = PlayerCharacter("Charly" , 22)
player2 = PlayerCharacter("Toby" , 23)
player2.attack = 99
player1.attack = 93

print(player1)
print(player2)
print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.run())
print(player1.attack)
print(player2.attack) 