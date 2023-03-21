class Contract:
    def __init__(self, declarer, bidColor, level, type, vulnerable = False):
        self.declarer = declarer
        self.bidColor = bidColor
        self.level = level
        self.type = type
        self.vulnerable = vulnerable

    @staticmethod
    def PASS():
        return Contract('', '', 0, '')

    def is_pass(self):
        return 0 == self.level
