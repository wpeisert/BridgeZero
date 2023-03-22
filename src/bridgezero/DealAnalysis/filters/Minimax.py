import copy

from bridgezero import constants
from bridgezero.Contract.Contract import Contract
from bridgezero.Contract.ContractService import ContractService


class Minimax:
    @staticmethod
    def filter(contractsEvaluated):
        bidding = []
        lastValue = 0
        while True:
            for side in constants.SIDES_NAMES:
                coeff = 1 if 'N' in side else -1
                maxContractEvaluated = Minimax.getMaxContractEvaluated(side, contractsEvaluated)
                if coeff * maxContractEvaluated['ev'] > coeff * lastValue:
                    lastValue = maxContractEvaluated['ev']
                    newContract = {
                        'side': side,
                        'contract': copy.deepcopy(maxContractEvaluated['contract']),
                        'ev': maxContractEvaluated['ev']
                    }
                else:
                    newContract = {
                        'side': side,
                        'contract': Contract.PASS(),
                        'ev': 0
                    }

                if newContract['contract'].is_pass() and len(bidding) > 0:
                    contractEvaluated = bidding.pop()
                    return contractEvaluated

                bidding.append(newContract)

                contractsEvaluated = Minimax.removeLowerContracts(contractsEvaluated, maxContractEvaluated['contract'])

    @staticmethod
    def getMaxContractEvaluated(side, contractsEvaluated):
        coeff = 1 if 'N' in side else -1
        index = None
        max = coeff * (-999999.0)
        for inx, contractEvaluated in enumerate(contractsEvaluated):
            if contractEvaluated['contract'].declarer not in side:
                continue
            if coeff * contractEvaluated['ev'] > coeff * max:
                max = contractEvaluated['ev']
                index = inx

        return contractsEvaluated[index]

    @staticmethod
    def removeLowerContracts(contractsEvaluated, contract: Contract):
        filteredContracts = {}
        for hash, contractEvaluated in contractsEvaluated.items():
            if ContractService.isLower(contractEvaluated['contract'], contract):
                continue
            filteredContracts[hash] = {
                'contract': copy.deepcopy(contractEvaluated['contract']),
                'ev': contractEvaluated['ev'],
            }

        return filteredContracts
