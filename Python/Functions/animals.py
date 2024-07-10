class Dog:
    def speak(self):
        print("Woof!")

    def __init__(self, name):
        self.name = name

    def hear(self, words):
        if self.name in words:
            self.speak()

class Husky(Dog):
    origin = "Siberia"

    def speak(self):
        print("Awoo!")

class Chihuahua(Dog):
    origin = "Mexico"
    def speak(self):
        print("Yip!")

class Labrador(Dog):
     origin = "Canada"
     def speak(self):
         print("Ruff!")
################################################################
class DogPark:
    def __init__(self, dogs):
        self.dogs = dogs

    def rollcall(self):
        print("Dogs in Park:")
        for dog in self.dogs:
            print(f"  {dog.name}")
        print()

    def shout(self, words):
        for dog in self.dogs:
            dog.hear(words)

    def converse(self):
        self.rollcall()
        while True:
            words = input("Talk to doggos! ('quit' to quit) > ")
            if 'quit' in words:
                print("Bye!")
                break
            else:
                # The shout method is used here.
                self.shout(words)

if __name__ == '__main__':
    dogs = [Husky("Toklat"),
            Chihuahua("Scrappy"),
            Labrador("Barrett")]
    park = DogPark(dogs)
    park.converse()