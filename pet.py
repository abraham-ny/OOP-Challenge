class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5 
        self.energy = 5  
        self.happiness = 5  
        self.tricks = []  

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger is now {self.hunger}, happiness is now {self.happiness}.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a nap. Energy is now {self.energy}.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played and had fun! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play. Try sleeping first.")

    def get_status(self):
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print("---------------------------")

    # Bonus methods
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}.")

    def show_tricks(self):
        print(f"{self.name} knows the following tricks:")
        if self.tricks:
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print("No tricks learned yet.")