from random import random


class Weapon:
    def __init__(self, type, attack_power):
        self.weapon_type = type
        self.attack_power = attack_power

    def selected_weapon(self):
        self.input = int(input("Enter a single digit number:"))
        player_weapon_number = int(input)
        num_to_select = 2
        self.weapon_type = {"Solar Blaster", "Sonar Evaporator", "Invisible Flood"}
        list_of_random_items_ = random.sample(self.weapon_type, num_to_select)
        first_random_item = list_of_random_items_[0]
        second_random_item = list_of_random_items_[1]
        if player_weapon_number % 2 == 0:
            self.weapon_type = first_random_item
            print(f"The power level assigned to your selected weapon is{self.weapon_type}")
        elif player_weapon_number % 2 != 0:
            self.weapon_type = second_random_item
            print(f"The power level assigned to your selected weapon is{self.weapon_type}")


    def attack_power(self):
        self.power = int(input("Enter a single digit number:"))
        player_power_number = int(input)
        num_to_select = 2
        self.attack_power = {10, 20, 30, 40, 50, 60, 70}
        list_of_random_items_ = random.sample(self.attack_power, num_to_select)
        first_random_item = list_of_random_items_[0]
        second_random_item = list_of_random_items_[1]
        if player_power_number % 2 == 0:
            self.attack_power = first_random_item
            print(f"The power level assigned to your selected weapon is{self.attack_power}")
        elif player_power_number % 2 != 0:
            self.attack_power = second_random_item
            print(f"The power level assigned to your selected weapon is{self.attack_power}")
