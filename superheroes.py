import random


class Ability:
    def __init__(self, name, max_damage):        
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)


class Hero:
    def __init__(self, name, starting_health=200):
        self.name = name
        self.abilities = []
        self.armors = []   
        self.starting_health = starting_health
        self.current_health = self.starting_health
        
    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        # self.block(damage_amt)
        block_total = 0
        for defend in self.armors:
            block_strength = defend.block()
            block_total += block_strength
        return block_total

    def attack(self):
        attack_total = 0
        for ability in self.abilities:
            attack_total += ability.attack() 
        return attack_total 

    def take_damage(self, damage):
        attack_check = self.attack() 
        defend_check = self.defend(damage)
        print("attack Check", attack_check)
        print("defend Check", defend_check)
        self.current_health = attack_check + defend_check
        print(f"current health is {self.current_health}")
            
    ''' Return True or False depending on whether the hero is alive or not. '''
    def is_alive(self):
        health = self.current_health 
        if health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in. '''

  # TODO: Fight each hero until a victor emerges.
  # Print the victor's name to the screen.
        #while a hero is still alive run attacks again
        #if is_alive is True. run                               
        #if is_alive is true after all attacks are done from both hero's. print DRAW
    pass
           


def create_duff_man():
    """ Hero object"""
    hero = Hero("Duff Man")

    """ Ability objects"""
    punch = Ability("punch", 60)
    kick = Ability("kicks", 70)
    hero.add_ability(punch)
    hero.add_ability(kick)

    """ Armor instance objects"""
    block = Armor("block!", 50)
    shield = Armor("shield block!", 70)
    hero.add_armor(block)
    hero.add_armor(shield)
    hero.defend(2)
    print(f"Defended {hero.defend(2)} points of damage")

    return hero

def create_grace_hopper():
    hero = Hero("Grace Hopper", 200)
    debugging = Ability("Great Debugging", 50)
    smarty_pants = Ability("Smarty Pants", 90)
    hero.add_ability(debugging)
    hero.add_ability(smarty_pants)
    return hero


""" Test cases """

def duff_man_battles_grace_hopper():
    duff_man = create_duff_man()
    grace = create_grace_hopper()
    for attack_number in range(1):
        duff_attack_power = duff_man.attack()
        grace_attack_power = grace.attack()
        print("Duff Man's attack:", duff_attack_power)
        print("Grace's attack:", grace_attack_power)

if __name__ == "__main__":
    duff_man_battles_grace_hopper()

    """ Deal damage to each hero """
        # duff_man.take_damage(grace_attack_power)
        # grace.take_damage(duff_attack_power)

        # Check if either hero died
        # if not duff_man.is_alive():
        #     print(grace.name, "won!")
        # elif ...:
        #     print()

if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())

# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     print(f"current health is {hero.current_health}")

# if __name__ == "__main__":
#     ability = Ability("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     print(hero.abilities)

# if __name__ == "__main__":
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.starting_health)

# if __name__ == "__main__":
#     print(ability.name)
#     print(ability.attack())