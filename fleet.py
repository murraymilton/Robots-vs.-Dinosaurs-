from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.robots = []
        self.weapons = []
        self.create_weapon()
        self.create_fleet()

    def create_weapon(self):
        manner = Weapon("Massmar Cannon", 100)
        winter = Weapon("Solar Blast", 100)
        star = Weapon("Sonar Flood", 100)
        self.weapons.append(manner)
        self.weapons.append(winter)
        self.weapons.append(star)

    def create_fleet(self):
        robot_one = Robot("Cyrus", self.weapons[0], 100)
        robot_two = Robot("Bill", self.weapons[1], 100)
        robot_three = Robot("Tom", self.weapons[2], 100)
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)






