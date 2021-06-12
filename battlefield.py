import random
from heard import Heard
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.import_fleet = Fleet()
        self.import_robot = Fleet()
        self.import_heard = Heard()
        self.import_dinosaur = Heard()
