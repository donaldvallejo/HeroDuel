#! user/bin/python
#capt. Alien is boss!
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
    def __init__(self, name, starting_health=100):
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
        self.current_health = self.current_health - (damage - self.defend(damage))
        print(f"current health is {self.current_health} \n")

    ''' Return True or False depending on whether the hero is alive or not. '''
    def is_alive(self):
        health = self.current_health
        if health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in. '''
        while self.current_health > 0 or opponent.current_health > 0:
            self.attack(opponent)
            opponent.attack(self)

        #aFTER ONE DIES:
        if self.current_health > 0:
            print(f" {self.name} is motherfucking victorious")
        else:
            print(f"{opponent.name} B is a badass bitch!!")


def create_duff_man():
    """ Hero object"""
    hero = Hero("Duff Man")

    """ Ability objects"""
    punch = Ability("drunk punch", 60)
    kick = Ability("kicks", 70)
    hero.add_ability(punch)
    hero.add_ability(kick)

    """ Armor instance objects"""
    block = Armor("block!", 50)
    shield = Armor("shield block!", 70)
    hero.add_armor(block)
    hero.add_armor(shield)
    hero.defend(2)
    print(f"Defended {hero.defend(2)} points of damage \n")
    return hero

def create_grace_hopper():
    hero = Hero("Grace Hopper", 200)
    debugging = Ability("Great Debugging", 50)
    smarty_pants = Ability("Smarty Pants", 90)
    hero.add_ability(debugging)
    hero.add_ability(smarty_pants)
    punch = Ability("punch", 60)
    kick = Ability("kicks", 70)
    hero.add_ability(punch)
    hero.add_ability(kick)

    """ Armor instance objects"""
    block = Armor("grace block!", 50)
    shield = Armor("grace shield block!", 70)
    hero.add_armor(block)
    hero.add_armor(shield)
    hero.defend(2)
    print(f"grace Defended {hero.defend(2)} points of damage \n")
    return hero


def battle():
    # 1)instantiate the fighters
    duff_man = Hero("Duff Man", 200)
    grace_hopper =Hero("Anisha", 500)
    # 2) make the figters fighter
    duff_man.fight(grace_hopper)
    # 3) lots of blood and gore



if __name__ == "__main__":
    battle()
