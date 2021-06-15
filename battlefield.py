

import battlefield
from heard import Heard
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.display_entry = "The last battle for existence: Robots vs Dinosaurs"
        print(self.display_entry)
        self.fleet = Fleet()
        self.robot_one_start = self.fleet.robots[0]
        self.robot_two_start = self.fleet.robots[1]
        self.robot_three_start = self.fleet.robots[2]

        self.heard = Heard()
        self.dinosaur_one_start = self.heard.dinosaurs[0]
        self.dinosaur_two_start = self.heard.dinosaurs[1]
        self.dinosaur_three_start = self.heard.dinosaurs[2]

    def game_start(self):
        game_user = input("Are you prepared to defend your fleet or heard? To accept enter 1")
        if game_user == "1":
            self.robot_one_start.health -= self.dinosaur_one_start.attack_power
            self.dinosaur_one_start.health -= self.robot_one_start.attack_power
            self.robot_one_start.power_level -= 20
            self.dinosaur_one_start.energy -= 20
            pass

    def victor_of_battle(self):
        if self.robot_one_start.health == 0 and self.robot_two_start.health == 0 and self.robot_three_start.health == 0:
            print("The dinosaurs have defeated the robots")
            if self.dinosaur_one_start.health == 0 and self.dinosaur_two_start.health == 0 and self.dinosaur_three_start.health == 0:
                print("The robots have desecrated the dinosaurs and claimed the victory!")

        # Need to make corrections
        # def battle(self):
        #     self.fleet.robots[0].robot_attack(self.heard.dinosaurs[1])
        #     self.heard.dinosaurs[0].dinosaur_attack(self.fleet.robots[2])
        # battlefield.Battlefield.battle(self)
        # battlefield.Battlefield.dinosaur_strikes(self)
        # battlefield.Battlefield.robot_strikes(self)
        # battlefield.Battlefield.view_dinosaur_opponent_options(self)
        # battlefield.Battlefield.view.robot_opponent_options(self)