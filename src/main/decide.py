"""Decide"""

from main.cmv import CMV
from main.fuv import FUV
from main.pum import PUM


class Decide:
    """Decide class

    :ivar: input: The input file.
    :type: input: dict.
    """

    def __init__(self, input):
        """Initializing the object.

        :param input: The input file.
        :type: input: dict.
        """
        self.input = input

    def decide(self):
        """Returning true if an interceptor should be launched based upon input radar tracking information.

        :returns: True if the method's conditions are satisfied otherwise return false.
        :rtype: bool
        """
        if not (2 <= self.input['NUMPOINTS'] <= 100):
            raise ValueError("The NUMPOINTS must be between two and one hundred.")
        cmv = CMV(self.input).calc_CMV()
        pum = PUM(self.input, cmv).calc_PUM()
        fuv = FUV(self.input, pum).calc_FUV()
        for i in range(len(fuv)):
            if fuv[i] is not True:
                return False
        return True

