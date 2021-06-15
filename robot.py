from weapon import Weapon


class Robot:
    def __init__(self, name, weapon, attack_power):
        self.name = name
        self.health = 100
        self.power_level = 100
        self.robot_weapon = weapon
        self.attack_power = attack_power

    def robot_attack(self, dinosaur):
        dinosaur.health -= self.robot_weapon.attack_power
        self.power_level -= 20





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



