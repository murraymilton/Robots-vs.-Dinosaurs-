from random import random


class Weapon:
    def __init__(self, type, attack_power):
        self.weapon_type = type
        self.attack_power = attack_power

    def selected_weapon(self):
        self.weapon_type = int(input("Enter a single digit number:"))
        print(f"The weapon assigned to your Robot: {self.weapon_type}")

    def attack_power(self):
        self.attack_power = int(input("Enter a single digit number:"))
        player_power_number = int(input)
        num_to_select = 2
        power_level = {10, 20, 30, 40, 50, 60, 70}
        list_of_random_items_ = random.sample(power_level, num_to_select)
        first_random_item = list_of_random_items_[0]
        second_random_item = list_of_random_items_[1]
        if player_power_number % 2 == 0:
            power_level = first_random_item
            print(f"The power level assigned to your selected weapon is{power_level}")
        elif player_power_number % 2 != 0:
            power_level = second_random_item
            print(f"The power level assigned to your selected weapon is{power_level}")

