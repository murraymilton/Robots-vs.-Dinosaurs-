from weapon import Weapon


class Robot:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.energy = 100
        self.weapon = ''

    def attack(self, dinosaur):
        #solar loom blast strikes dinosaur reducing health level
        pass

    def robot_name(self):
        self.name = input("How shall we call your robot?")
        print(f" Prepare for battle {self.name}")

    def weapon_selected(self):
        self.weapon = Weapon
        self.weapon.selected_weapon()
        self.weapon.attack_power()
