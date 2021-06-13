from random import random


class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.health = 100
        self.energy = 100
        self.attack_power = attack_power

    def dinosaur_type(self):
        self.type = input("How shall we call your your dinosaur?")
        print(f"You must prevent the extinction of your heard {self.type}")


    def attack_power(self, number):
        #robot's health droid level goes down
        self.attack_power = input("Enter a single digit even number or odd number")
        num_to_select = 2
        level = {10, 20, 30, 40, 50, 60, 70}
        list_of_random_items_ = random.sample(level, num_to_select)
        first_random_item = list_of_random_items_[0]
        second_random_item = list_of_random_items_[1]
        if input % 2 == 0:
            self.attack_power = first_random_item
        elif input % 2 != 0:
            self.attack_power = second_random_item
        else:
            print("That is not a number!")

        #Need to review conditional statement  for random generation of power level.



