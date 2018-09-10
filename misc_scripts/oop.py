class Animal(object):
    def __init__(self,intelligence,cuteness):
        self.intelligence = intelligence
        self.cuteness = cuteness

    def fight(self,opponent):
        opponent.cuteness = opponent.cuteness - 2
        self.cuteness = self.cuteness - 1

class Cat(Animal):

    def __init__(self,intelligence,cuteness):

        intelligence = intelligence + 1
        super(Cat,self).__init__(intelligence, cuteness)

    # pass

# peter = Cat(8, 7)
# helga = Cat(7, 10)

# print("Intelligence:",peter.intelligence)
# print("Helga's Cuteness:",helga.cuteness)
# print("Peter's Cuteness:",peter.cuteness)
# print("Fight!")
# peter.fight(helga)
# print("Helga's Cuteness:",helga.cuteness)
# print("Peter's Cuteness:",peter.cuteness)


class device(object):
    def __init__(self, power):
        self.power = power
        self.sound = "Beep boop!"

    def start():

        if self.power is 1:
            print(self.sound)
            print("Booting successfull")
            return True
        else:
            print("Booting failed")
            return False

class laptop(device):
    def __init__(self, pwd, power):
        self.pwd = pwd

        super(laptop,self).__init__(power)

    def login():

        self.check_pwd = "hello"

        if self.pwd is self.check_pwd:
            print("Login successfull")
        else:
            print("Login failed")





yoga = laptop("hello", 1)
if yoga.start() is True:
    yoga.login()

# yoga.login("hello")
# print(yoga.sound)
