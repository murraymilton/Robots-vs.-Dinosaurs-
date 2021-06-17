from fleet import Fleet
from heard import Heard



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

    def dino_turn(self):
        print("Choose the dinosaur who will attack:")
        self.show_dino_opponent_options()
        chosen_dino = int(input())
        print("Choose the robot who will defend:")
        self.show_robo_opponent_options()
        chosen_robot = int(input())
        self.herd.dinosaurs[chosen_dino].attack(self.fleet.robots[chosen_robot])
        if self.fleet.robots[chosen_robot].health <= 0:
            print(f"{self.fleet.robots[chosen_robot]} has died")
            self.fleet.robots.remove(self.fleet.robots[chosen_robot])

    def robo_turn(self):
        print("Choose the robot who will attack:")
        self.show_robo_opponent_options()
        chosen_robot = int(input())
        print("Choose the dinosaur who will defend:")
        self.show_dino_opponent_options()
        chosen_dino = int(input())
        self.fleet.robots[chosen_robot].attack(self.herd.dinosaurs[chosen_dino])
        if self.herd.dinosaurs[chosen_dino].health <= 0:
            print(f"{self.herd.dinosaurs[chosen_dino]} has died")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[chosen_dino])

    def show_dino_opponent_options(self):
        dino_index = 0
        for dino in self.herd.dinosaurs:
            print(f"Press {dino_index} for {dino.type}")
            dino_index += 1

    def show_robo_opponent_options(self):
        robot_index = 0
        for robot in self.fleet.robots:
            print(f"Press {robot_index} for {robot.name}")
            robot_index += 1


    def victor_of_battle(self):
        if self.robot_one_start.health == 0 and self.robot_two_start.health == 0 and self.robot_three_start.health == 0:
            print("The dinosaurs have defeated the robots")
            if self.dinosaur_one_start.health == 0 and self.dinosaur_two_start.health == 0 and self.dinosaur_three_start.health == 0:
                print("The robots have desecrated the dinosaurs and claimed the victory!")

