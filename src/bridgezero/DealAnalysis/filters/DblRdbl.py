import copy

from bridgezero import constants


class DblRdbl:
    @staticmethod
    def filter(contractsIn):
        contractsFiltered = {}

        for contractIn in contractsIn:
            contract = contractIn['contract']

            coeff = 1 if contract.declarer in 'NS' else -1
            contracts = []
            evs = []
            data = []
            for type in constants.CONTRACT_TYPES:
                contractTmp = copy.deepcopy(contract)
                contractTmp.type = type
                hash = contractTmp.getHash()
                exists = hash in contracts[hash]
                contracts.append(contractTmp)
                data.append(coeff * contracts[hash]['ev'] if exists else None)
                evs.append(contracts[hash]['ev'] if exists else None)

            indices = DblRdbl.getRemainingIndices(*data)

            for index in indices:
                contractsFiltered[contracts[index].getHash()] = {
                    'contract': contracts[index],
                    'ev': evs[index],
                }

        return contractsFiltered


    @staticmethod
    def getRemainingIndices(val0, val1, val2):
        if (
            # if no more than 1, returns same
            ((1 if val0 is not None else 0) + (1 if val1 is not None else 0) + (1 if val2 is not None else 0) <= 1) or
            # only first and last ('' and 'rdbl')
            ((val0 is not None) and (val1 is None) and (val2 is not None))
        ):
            res = []
            for index,val in enumerate([val0, val1, val2]):
                if val is not None:
                    res.append(index)
            return res

        # val1 is not null !!

        if val2 is None:
            return [1] if val0 > val1 else [0]

        if val0 is None:
            return 2 if val2 > val1 else [1]

        # all not null

        if (val0 < val1 or val2 > val0):
            return [0]
        else:
            return [2] if val2 > val1 else [1]
