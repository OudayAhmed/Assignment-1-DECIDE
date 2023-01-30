"""Final Unlocking Vector (FUV)"""


class FUV:
    """Final Unlocking Vector (FUV) class.

        :ivar: puv: Preliminary Unlocking Vector
        :type: puv: 1D array (14*1).
        :ivar: pum: Preliminary Unlocking Matrix
        :type: pum: 2D array (14*14).
    """

    def __init__(self, puv, pum):
        self.puv = puv
        self.pum = pum

    @staticmethod
    def fuv(puv, pum):
        """ Checking FUV[i], which should be set to true if
        1)PUV[i] is false, or
        2)all elements in PUM row i are true

        """

        FUV = []
        for i in range(14):
            if not puv[i]:
                FUV.append(True)
                continue
            else:
                all_true = True
                for j in range(14):
                    if j != i:
                        if not pum[i][j]:
                            all_true = False
                            break
                FUV.append(all_true)
        return FUV

    def calc_FUV(self):
        return self.fuv(self.puv, self.pum)
