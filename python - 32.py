class PlayerCharacter:
    membership = True
    def __init__(self , name , age):
        if (PlayerCharacter.membership):
           self.name = name
           self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self):
        print(f'my nameis {self.name}') 

    @classmethod
    def adding_things1(cls , num1 , num2):
        return cls("Teddy" , num1 + num2)

    @staticmethod
    def adding_things2(num1 , num2):
        return num1 + num2  

player1 = PlayerCharacter("Charly" , 22)
player2 = PlayerCharacter("Toby" , 23)
player2.attack = 99
player1.attack = 93
print(player1.shout())
print(player2.run())
print(player1.adding_things1(2, 3).age)
player3 = PlayerCharacter.adding_things1(2 , 3)
print(player3.age)       