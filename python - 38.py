class User():
    def __init__(self , email):
        self.email = email
        

    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self , name , power , email):
        super().__init__(email) #user can also be used instaed of super() and the self is not neede if super() is used
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
wizard2 = Wizard("Mickey", 70 , "mickey2008@gmail.com")
print(wizard2.email)
print(dir(wizard1))