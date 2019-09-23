class Hero:
    def __init__(self, name, starting_health):
        self.name = name
        self.starting_health = starting_health
        
    def add_ability(self, ability):
        self.add_ability = add_ability
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