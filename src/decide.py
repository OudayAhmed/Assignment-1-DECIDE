from src.cmv import CMV


class Decide:
    def __init__(self, input):
        self.input = input

    def decide(self):
        cmv = CMV(self.input).calc_CMV()
        print(cmv)
