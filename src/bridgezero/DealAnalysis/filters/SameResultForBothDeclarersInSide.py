import copy

from bridgezero.Bidding.Tools import Tools


class SameResultForBothDeclarersInSide:
    @staticmethod
    def filter(contractsIn):
        contractsFiltered = {}

        for hash1, contractIn in contractsIn.items():
            contract1 = copy.deepcopy(contract['contract'])
            ev1 = contractIn['ev']

            contract2 = contractIn['contract']
            contract2.declarer = Tools.getPartner(contract2.declarer)
            hash2 = contract2.getHash()

            if hash2 not in contractsFiltered:
                contractsFiltered[hash1] = {
                    'contract': contract1,
                    'ev': ev1,
                }
            continue

            ev2 = contractsIn[hash2]['ev']

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
