from game.battle.commoon.skill import Skill
from game.character.common.character import Character

class Spell(Skill):
    def __init__(self, use_mp:int, power:int, name:str):
        self.use_mp = use_mp
        self.power = power
        self.effect = None
        self.element = 'No element'
        self.name = name

        super().__init__(self.name)


    def use_spell(self, user:Character, target:Character):
        user.mp = user.mp - self.use_mp
        target.hp = target.hp - (self.power * user.magic_attack - target.magic_difence)
        print(user.name, "used", self.name, "to", target.name, "!")
        if target.hp <= 0:
            target.hp = 0
            print(target, "died !")

    def set_element(self, new_element:str):
        self.element = new_element

    def get_element(self):
        return self.element

    def get_use_mp(self):
        return self.use_mp
