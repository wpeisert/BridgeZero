import copy

from bridgezero.Bidding.Tools import Tools


class SameResultForBothDeclarersInSide:
    @staticmethod
    def filter(contractsEvaluated):
        contractsFiltered = {}

        for hash1, contractEvaluated in contractsEvaluated.items():
            contract1 = copy.deepcopy(contractEvaluated['contract'])
            ev1 = contractEvaluated['ev']

            contract2 = contractEvaluated['contract']
            contract2.declarer = Tools.getPartner(contract2.declarer)
            hash2 = contract2.getHash()

            if hash2 not in contractsFiltered:
                contractsFiltered[hash1] = {
                    'contract': contract1,
                    'ev': ev1,
                }
            continue

            ev2 = contractsEvaluated[hash2]['ev']

            if abs(ev1 - ev2) < 0.001:
                contract1.declarer = Tools.getFirstPlayerInSide(contract1.declarer)
                hash1 = contract1.getHash()
                contractsFiltered[hash1] = {
                    'contract': contract1,
                    'ev': ev1,
                }

                continue

            contractsFiltered[hash1] = {
                'contract': contract1,
                'ev': ev1,
            }

            contractsFiltered[hash2] = {
                'contract': contract2,
                'ev': ev2,
            }

        return contractsFiltered
