from bridgezero import constants
from bridgezero.Contract.Contract import Contract


class ContractValueService:
    """
    https://www.pzbs.pl/sedziowie/mpb/2007/pol/przep77.htm
    calculator: https://www.funbridge.com/counting-bridge
    """
    @staticmethod
    def getContractValue(contract: Contract, tricks: int):
        if contract.is_pass():
            return 0

        requiredTricks = constants.BASE_TRICKS + contract.level
        if tricks < requiredTricks:
            value = - ContractValueService.getPenaltyValue(requiredTricks - tricks, contract.type, contract.vulnerable)
        else:
            value = ContractValueService.getSuccessValue(contract.bidColor, contract.level, tricks, contract.type, contract.vulnerable)

        if contract.declarer in 'EW':
            value = -value

        return value

    @staticmethod
    def getPenaltyValue(tricksBelow: int, type: str, vulnerable: bool):
        value = constants.PENALTY_FIRST_UNDERTRICK[vulnerable][type] + \
            (tricksBelow - 1) * constants.PENALTY_SECOND_UNDERTRICK[vulnerable][type]
        if tricksBelow >= constants.PENALTY_FOURTH_FROM:
            value += (tricksBelow - constants.PENALTY_FOURTH_FROM + 1) * constants.PENALTY_FOURTH_UNDERTRICK[vulnerable][type]

        return value

    @staticmethod
    def getSuccessValue(bidColor: str, level: int, tricks: int, type: str, vulnerable: bool):
        declaredValue = constants.REWARD_FIRST_TRICK[bidColor] + \
            (level - 1) * constants.REWARD_NEXT_TRICK[bidColor]
        if type == 'dbl':
            declaredValue *= 2
        elif type == 'rdbl':
            declaredValue *= 4

        value = declaredValue

        isGame = declaredValue >= constants.GAME_REQUIRED_POINTS
        if isGame:
            value += constants.REWARD_GAME[vulnerable]
        else:
            value += constants.REWARD_NONGAME

        value += constants.REWARD_DBL[type]
        value += constants.REWARD_SLAM[vulnerable].get(level, 0)

        overtricks = tricks - constants.BASE_TRICKS - level

        if ('' == type):
            value += overtricks * constants.REWARD_NEXT_TRICK[bidColor]
        else:
            value += overtricks * constants.REWARD_OVERTRICKS_DBL[vulnerable][type]

        return value
