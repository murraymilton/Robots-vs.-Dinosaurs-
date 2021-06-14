from weapon import Weapon


class Robot:
    def __init__(self, attack_power):
        self.create_name = []
        self.health = 100
        self.power_level = 100
        self.assign_robot()
        self.weapons = []
        self.attack_power = attack_power

    def attack_power(self, dinosaur_injury):
        dinosaur_injury.health -= self.weapons[0].attack_power
        dinosaur_injury.health -= self.weapons[1].attack_power
        dinosaur_injury.health -= self.weapons[2].attck_power

        return dinosaur_injury
        pass

    def create_name(self):
        self.create_name = input("How shall we call your Robot?")
        robot_one = self.create_name
        print(f"Your robot is {robot_one} ")

    def assign_robot(self):
        manner = Weapon("Rifle", 100)
        winter = Weapon("Solar Blast", 100)
        star = Weapon("Sonar Flood", 100)
        self.weapons.append(manner)
        self.weapons.append(winter)
        self.weapons.append(star)



    #
    # def robot_name(self):
    #     robot_one = Robot("How shall we call your Robot?")
    #     print(f"Prepare for battle {robot_one}")
    #     robot_two = Robot("How shall we call your Robot?")
    #     print(f"Prepare for battle {robot_two}")
    #     robot_three = Robot("How shall we call your Robot?")
    #     print(f"Prepare for battle {robot_three}")
        # self.robot_name
        # self.robot_name.append(robot_two)
        # self.robot_name.append(robot_three)


















    # #solar loom blast strikes dinosaur reducing health level
    # pass

    # how will the robot lose health? Write a method  for counting or monitorying



    # #solar loom blast strikes dinosaur reducing health level
    # pass

    # def weapon_selected(self):
    #     self.weapon = Weapon
    #     self.weapon.selected_weapon()
    #
    #     self.weapon.attack_power()



