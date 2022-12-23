from game.character.common.character import Character


class Enemy(Character):
    def __init__(self, 
                 name: str, 
                 hp: int, 
                 mp: int, 
                 attack: int, 
                 difence: int, 
                 magic_attack: int, 
                 magic_difence: int, 
                 speed: int, 
                 skill: dict, 
                 experiment: int,
                 level_experiment:list,
                 growth_type:list,
                 image):
        self.experiment = experiment
        super().__init__(name, hp, mp, attack, difence, magic_attack, magic_difence, speed, skill, level_experiment, growth_type, image)

    def get_experiment(self):
        return self.experiment
