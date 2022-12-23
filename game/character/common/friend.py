from game.battle.commoon.skill import Skill
from game.character.common.character import Character

class Friend(Character):
    def __init__(self, character_type:Character):
        self.character_type = character_type
        self.name = character_type.name
        self.personality = 'tinkering'

        self.hp = character_type.hp
        self.mp = character_type.mp
        self.attack = character_type.attack
        self.difence = character_type.difence
        self.magic_attack = character_type.magic_attack
        self.magic_difence = self.character_type.magic_difence
        self.speed = character_type.speed
        self.skill = character_type.skill
        self.image = character_type.image
        self.level_experiment = character_type.level_experiment
        self.growth_type = character_type.growth_type
        self.experiment = 0
        self.all_experiment = 0

        super().__init__(self.name, 
                         self.hp, 
                         self.mp, 
                         self.attack, 
                         self.difence, 
                         self.magic_attack, 
                         self.magic_difence, 
                         self.speed, 
                         self.skill,
                         self.level_experiment,
                         self.growth_type,
                         self.image)

    def set_name(self, new_name:str):
        self.name = new_name

    def level_up(self):       
        if self.level == 100:
            print("you reach to the max level!")
        else:
            self.level = self.level + 1

        for i in self.skill:
            if i <= self.level:
                self.skill_list[self.skill[i].get_name()] = self.skill[i]
                print(self.name, "learned", self.skill[i].get_name())
            else:
                break

    def learn_spell(self, skill:Skill):
        self.skill_list[skill.get_name()] = skill

    def add_experiment(self, get:int):
        self.experiment = self.experiment + get
        self.all_experiment = self.all_experiment + get
        while True:
            if self.experiment < self.level_experiment[0]:
                break
            else:
                self.level_up()
                self.experiment = self.experiment - self.level_experiment[0]
                self.level_experiment.remove(self.level_experiment[0])

    def get_experiment(self):
        return self.experiment

    def get_all_experiment(self):
        return self.all_experiment

    def get_next_experiment(self):
        return self.level_experiment[0] - self.experiment

