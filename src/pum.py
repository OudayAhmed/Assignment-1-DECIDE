"""Preliminary Unlocking Matrix (PUM)"""

class PUM:
    """Preliminary Unlocking Matrix (PUM) class

    :ivar: input: The input file.
    :type: input: dict.
    :ivar: CMV: The Conditions Met Vector (CMV).
    :type: CMV: 1Darray (floats)
    :ivar: LCM: Logical Connector Matrix (LCM).
    :type: LCM: 2Darray (string)
    """

    def __init__(self, input, cmv):
        """Initializing the object.

        :param input: The input file.
        :type: input: dict.
        :param cmv: The Conditions Met Vector (CMV).
        :type: cmv: 1Darray (floats)
        """
        self.input = input
        self.CMV = cmv
        self.LCM = input['LCM']

    def calc_PUM(self):
        """Calculating and returning the preliminary unlocking matrix (PUM).

        :returns: The preliminary unlocking matrix (PUM).
        :rtype: 2Darray (int)
        """
        if len(self.CMV) != 15:
            raise ValueError("The Conditions Met Vector (CMV) length must be fifteen.")
        if len(self.LCM) != 15 or len(self.LCM[0]) != 15:
            raise ValueError("The number of rows and columns within the Logical Connector Matrix (LCM) must be fifteen.")
        for i in range(len(self.LCM)):
            for j in range(len(self.LCM[0])):
                if self.LCM[i][j] != self.LCM[j][i]:
                    raise ValueError("The Logical Connector Matrix (LCM) must be symmetric.")
        PUM = []
        for i in range(15):
            c = []
            for j in range(15):
                if i == j:
                    c.append(-1)
                elif self.LCM[i][j] == 'NOTUSED':
                    c.append(1)
                elif self.LCM[i][j] == 'ANDD':
                    if self.CMV[i] and self.CMV[j]:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if self.CMV[i] or self.CMV[j]:
                        c.append(1)
                    else:
                        c.append(0)
            PUM.append(c)
        return PUM