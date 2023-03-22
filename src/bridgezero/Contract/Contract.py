from bridgezero import constants


class Contract:
    def __init__(self, **kwargs):
        self.declarer = kwargs.get('declarer')
        self.bidColor = kwargs.get('bidColor')
        self.level = kwargs.get('level')
        self.type = kwargs.get('type', '')
        self.vulnerable = kwargs.get('vulnerable', False)

    @staticmethod
    def PASS():
        return Contract(level=0)

    def is_pass(self):
        return 0 == self.level

    def getHash(self):
        if self.is_pass():
            return 'pass'

        return Contract.calculateHash(self.declarer, self.level, self.bidColor, self.type, self.vulnerable)

    @staticmethod
    def calculateHash(declarer: str, level: int, bidColor: str, type: str, vulnerable: bool):
        return declarer + str(level) + bidColor + type + ('(vuln)' if vulnerable else '')
