import random
import requests

class Character:
    def __init__(self, name, race, char_class, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Race: {self.race}\n"
                f"Class: {self.char_class}\n"
                f"Strength: {self.strength}\n"
                f"Dexterity: {self.dexterity}\n"
                f"Constitution: {self.constitution}\n"
                f"Intelligence: {self.intelligence}\n"
                f"Wisdom: {self.wisdom}\n"
                f"Charisma: {self.charisma}\n")

def roll_dice():
    return random.randint(1, 6)

def roll_stat():
    rolls = [roll_dice() for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)

def randomize_character():
    names = ["Aragorn", "Legolas", "Gimli", "Frodo", "Gandalf"]
    races = ["Human", "Elf", "Dwarf", "Hobbit", "Wizard"]
    def get_random_name():
        response = requests.get("https://randomuser.me/api/")
        if response.status_code == 200:
            data = response.json()
            return data['results'][0]['name']['first']
        else:
            return "Unknown"

    names = [get_random_name() for _ in range(5)]
    classes = ["Warrior", "Archer", "Berserker", "Thief", "Mage"]

    name = random.choice(names)
    race = random.choice(races)
    char_class = random.choice(classes)
    strength = roll_stat()
    dexterity = roll_stat()
    constitution = roll_stat()
    intelligence = roll_stat()
    wisdom = roll_stat()
    charisma = roll_stat()

    return Character(name, race, char_class, strength, dexterity, constitution, intelligence, wisdom, charisma)

if __name__ == "__main__":
    character = randomize_character()
    print(character)