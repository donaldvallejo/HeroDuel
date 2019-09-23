# import heros
import random

class Hero:
    def __init__(self, name, starting_health=200):
        self.name = name
        self.starting_health = starting_health
        
    def add_ability(self, ability):
        self.ability = ability
        return

class Ability:
    def __init__(self, name, attack_strength):        
        self.name = name
        self.attack_strength = attack_strength
        
    def attack(self):
        attack = random.randint(0, ability.max_damage)
        print(attack)
        return

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        block = random.randint(0, armor.max_block)
        print(block)
        return

""" hero instance variables"""
my_hero = Hero("Duff Man", 100)
my_hero.abilities = ["Punch", "kick", "drink"]
my_hero.armors = []
my_hero.name = ""
my_hero.current_health = 50
my_hero.starting_health = 200

""" ability instance variables"""
ability.self.append("punch again")
# ability = Ability("Punch again!", 50)
ability.max_damage = 200

""" armor instance variables"""
armor = Armor("block!", 50)
armor.max_block = 200

""" Test cases """
if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    my_hero = Hero("Grace Hopper", 200)
    my_hero.add_ability(ability)
    print(my_hero.abilities)

# if __name__ == "__main__":
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.starting_health)

# if __name__ == "__main__":
#     ability = Ability("Debugging Ability", 20)
#     print(ability.name)
#     print(ability.attack())