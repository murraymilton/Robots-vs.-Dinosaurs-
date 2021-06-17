class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.health = 100
        self.energy = 100
        self.attack_power = attack_power

    def dino_attack(self, robot):
            robot.health -= self.dinosaur.attack_power
            self.energy -= 20
            print(f"{self.type} attacks {robot.name} for {self.attack_power} damage. New health is {robot.health}.")










    # def attack_power(self, robot_damage):
    #     robot_damage.health -= self.attack_power
    #     robot_damage.health -= self.attack_power
    #     robot_damage.health -= self.attack_power

    # def __init__(self, name, weapon, attack_power):
    #     self.name = name
    #     self.health = 100
    #     self.power_level = 100
    #     self.robot_weapon = weapon
    #     self.attack_power = attack_power
    #
    # def robot_attack(self, dinosaur):
    #     dinosaur.health -= self.robot_weapon.attack_power
    #     self.power_level -= 20































  # def attack_power(self, number):
    #     #robot's health droid level goes down
    #     self.attack_power = input("Enter a single digit even number or odd number")
    #     num_to_select = 2
    #     level = {10, 20, 30, 40, 50, 60, 70}
    #     list_of_random_items_ = random.sample(level, num_to_select)
    #     first_random_item = list_of_random_items_[0]
    #     second_random_item = list_of_random_items_[1]
    #     if input % 2 == 0:
    #         self.attack_power = first_random_item
    #     elif input % 2 != 0:
    #         self.attack_power = second_random_item
    #     else:
    #         print("That is not a number!")

        #Need to review conditional statement  for random generation of power level.



