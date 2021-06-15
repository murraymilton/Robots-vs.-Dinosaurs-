from heard import Heard
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.display_entry = "The last battle for existence: Robots vs Dinosaurs"
        print(self.display_entry)
        self.fleet = Fleet()
        self.robot_one_start = self.fleet.robots[1]
        self.robot_two_start = self.fleet.robots[2]
        self.robot_three_start = self.fleet.robots[3]


        self.heard = Heard()
        self.dinosaur_one_start = self.heard.dinosaurs[0]
        self.dinosaur_one_start = self.heard.dinosaurs[1]
        self.dinosaur_one_start = self.heard.dinosaurs[2]

    # def game_start(self):
    #     battlefield.Battlefield.battle(self)
    #     battlefield.Battlefield.dinosaur_strikes(self)
    #     battlefield.Battlefield.robot_strikes(self)

    pass


    def battle(self):
        self.fleet.robots[0].robot_attack(self.heard.dinosaurs[1])
        self.heard.dinosaurs[0].dinosaur_attack(self.fleet.robots[2])
        pass


