class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} enjoyed a tasty meal!")
        else:
            print(f"{self.name} is already full.")

    def sleep(self):
        if self.energy < 10:
            self.energy = min(10, self.energy + 5)
            print(f"{self.name} had a refreshing nap.")
        else:
            print(f"{self.name} is fully rested.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} had a great time playing!")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print(f"Tricks learned: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
        print("-------------------------\n")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"\n--- {self.name}'s Tricks ---")
            for trick in self.tricks:
                print(f"- {trick}")
            print("-------------------------\n")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

if __name__ == "__main__":
    my_pet = Pet("Buddy")

    my_pet.get_status()

    my_pet.eat()
    my_pet.play()
    my_pet.get_status()

    my_pet.sleep()
    my_pet.get_status()

    my_pet.train("fetch")
    my_pet.train("roll over")
    my_pet.show_tricks()

    my_pet.play()
    my_pet.eat()
    my_pet.get_status()

    my_pet.train("speak")
    my_pet.show_tricks()