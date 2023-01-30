from src.cmv import CMV
from src.fuv import FUV


class Decide:
    def __init__(self, input):
        self.input = input

    def decide(self):
        cmv = CMV(self.input).calc_CMV()
        print(cmv)

        fuv = FUV(self.puv, self.pum).calc_FUV()
