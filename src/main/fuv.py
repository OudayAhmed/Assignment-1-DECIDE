"""Final Unlocking Vector (FUV)"""


class FUV:
    """Final Unlocking Vector (FUV) class.

        :ivar: input: The input file.
        :type: input: dict.
        :ivar: puv: Preliminary Unlocking Vector
        :type: puv: 1D array (15*1).
        :ivar: pum: Preliminary Unlocking Matrix
        :type: pum: 2D array (15*15).
    """

    def __init__(self, input, pum):
        """Initializing the object.

        :ivar: input: The input file.
        :type: input: dict.
        :ivar: pum: Preliminary Unlocking Matrix
        :type: pum: 2D array (15*15).
        """
        self.input = input
        self.pum = pum
        self.puv = input["PUV"]

    @staticmethod
    def fuv(puv, pum):
        """ Checking FUV[i], which should be set to true if
        1)PUV[i] is false, or
        2)all elements in PUM row i are true

        :returns: The Final Unlocking Vector (FUV).
        :rtype: 1D array (15*1)
        """


        FUV = []
        for i in range(15):
            if not puv[i]:
                FUV.append(True)
                continue
            else:
                all_true = True
                for j in range(15):
                    if j != i:
                        if not pum[i][j]:
                            all_true = False
                            break
                FUV.append(all_true)
        return FUV

    def calc_FUV(self):
        if len(self.puv) != 15:
            raise ValueError("The length of PUV must be fifteen.")
        if len(self.pum) != 15 or len(self.pum[0]) != 15:
            raise ValueError("The number of rows and columns within PUM must be fifteen.")
        return self.fuv(self.puv, self.pum)
