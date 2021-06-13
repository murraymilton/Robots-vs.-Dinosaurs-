import random
from heard import Heard
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.import_fleet = Fleet()
        self.import_fleet.robot_fleet()
        self.import_heard = Heard()
        self.import_dinosaur = Heard()
