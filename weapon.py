class Weapon:
    def __init__(self, type, attack_power):
        self.type = type
        self.attack_power = attack_power

    def battle(self):
        print(f"Your weapon of choice is {self.type} It has an attack power of {self.attack_power}")

























    # from random import random


    # def selected_weapon(self):
    #     self.player_weapon_number = int(input("Enter a number:"))
    #     player_weapon_number = input
    #     num_to_select = 2
    #     self.weapon_type = {"Solar Blaster", "Sonar Evaporator", "Invisible Flood"}
    #     list_of_random_items_ = random.sample(self.weapon_type, num_to_select)
    #     first_random_item = list_of_random_items_[0]
    #     second_random_item = list_of_random_items_[1]
    #     if player_weapon_number % 2 == 0:
    #         self.weapon_type = first_random_item
    #         print(f"The power level assigned to your selected weapon is{self.weapon_type}")
    #     elif player_weapon_number % 2 != 0:
    #         self.weapon_type = second_random_item
    #         print(f"The power level assigned to your selected weapon is{self.weapon_type}")
    #
    #
    # def attack_power(self):
    #     self.power = int(input("Enter               number:"))
    #     player_power_number = input
    #     num_to_select = 2
    #     self.attack_power = {10, 20, 30, 40, 50, 60, 70}
    #     list_of_random_items_ = random.sample(self.attack_power, num_to_select)
    #     first_random_item = list_of_random_items_[0]
    #     second_random_item = list_of_random_items_[1]
    #     if int(player_power_number) % 2 == 0:
    #         self.attack_power = first_random_item
    #         print(f"The power level assigned to your selected weapon is{self.attack_power}")
    #     elif int(player_power_number) % 2 != 0:
    #         self.attack_power = second_random_item
    #         print(f"The power level assigned to your selected weapon is{self.attack_power}")
