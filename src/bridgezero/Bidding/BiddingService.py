from bridgezero.Bidding.BiddingParser import BiddingParser
from bridgezero.Bidding.Tools import Tools
from bridgezero.Contract.ContractValueService import ContractValueService


class BiddingService:
    @staticmethod
    def calculateResults(deal, bidding):
        actualContract = BiddingParser.getContractWithoutVulnerability(bidding)
        res = {'contract': actualContract.getHash()}
        minimaxEv = deal.analysis.minimax_ev_NS

        if actualContract.isPass():
            ev = 0
        else:
            tricksProbabilities = deal.analysis['tricks_probabilities_NS']
            declarerPair = Tools.getPlayerSide(actualContract.declarer)
            vulnerableFieldName = 'vulnerable_' + declarerPair
            actualContract.vulnerable = getattr(deal, vulnerableFieldName)
            ev = ContractValueService.calculateContractExpectedValue(
                actualContract,
                tricksProbabilities.getProbabilities(actualContract.declarer, actualContract.bidColor)
            )

            res = ev - minimaxEv

        return res
