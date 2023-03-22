from bridgezero import constants
from bridgezero.Contract.Contract import Contract
from bridgezero.Contract.ContractValueService import ContractValueService


class ContractService:
    @staticmethod
    def evaluateContracts(contracts, tricksProbabilities):
        contractsEvaluated = []

        for contract in contracts:
            ev = ContractValueService.getContractValue(
                contract,
                tricksProbabilities.getProbabilities(contract.declarer, contract.bidColor)
            )

            contractsEvaluated. append(
                {
                    'contract': contract,
                    'ev': ev
                }
            )

        return contractsEvaluated


    @staticmethod
    def getAllContracts(**kwargs):
        sides = kwargs.get('sides', constants.SIDES_NAMES)
        levels = kwargs.get('levels', range(1, constants.BIDS_MAX_LEVEL))
        bidColors = kwargs.get('bidColors', constants.BIDS_COLORS)
        contractTypes = kwargs.get('contractTypes', constants.CONTRACT_TYPES)
        declarers = kwargs.get('declarers', constants.PLAYERS_NAMES)
        vulnerable_NS = kwargs.get('vulnerable_NS', False)
        vulnerable_EW = kwargs.get('vulnerable_EW', False)

        contracts = []

        for side in sides:
            for level in levels:
                for bidColor in bidColors:
                    for type in contractTypes:
                        for declarer in side:
                            if declarer not in declarers:
                                continue

                            vulnerable = vulnerable_NS if declarer in 'NS' else vulnerable_EW
                            contracts.append(
                                Contract(declarer=declarer, bidColor=bidColor, level=level, type=type, vulnerable=vulnerable)
                            )

        return contracts
