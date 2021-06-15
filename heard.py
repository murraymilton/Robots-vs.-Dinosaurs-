from dinosaur import Dinosaur


class Heard:
    def __init__(self):
        self.dinosaurs = []
        self.dinosaur_heard()


    def dinosaur_heard(self):
        dinosaur_one = Dinosaur("Rexisorius", 100)
        dinosaur_two = Dinosaur("Theropods", 100)
        dinosaur_three = Dinosaur("Barosuaurus", 100)
        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)


