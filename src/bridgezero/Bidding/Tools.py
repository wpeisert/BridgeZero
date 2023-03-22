from bridgezero import constants


class Tools:
    @staticmethod
    def getPlayerSide(playerName):
        for side in constants.SIDES_NAMES:
            if playerName in side:
                return side

    @staticmethod
    def getPartner(playerName):
        index = constants.PLAYERS_NAMES.index(playerName)
        index += 1 if index%2==0 else -1
        return constants.PLAYERS_NAMES[index]

    @staticmethod
    def getFirstPlayerInSide(playerName):
        for side in constants.SIDES_NAMES:
            if playerName in side:
                return side[0]
