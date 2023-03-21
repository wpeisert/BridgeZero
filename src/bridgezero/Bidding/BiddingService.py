from bridgezero.Bidding.BiddingParser import BiddingParser
from bridgezero.Bidding.Tools import Tools
from bridgezero.Contract.ContractValueService import ContractValueService
from bridgezero.DealAnalysis.DealAnalyser import DealAnalyser


class BiddingService:
    @staticmethod
    def calculate_ns_result(deal, bidding):
        actualContract = BiddingParser.getContractWithoutVulnerability(deal, bidding)
        if not len(deal.analysis):
            DealAnalyser.analyseDeal(deal)
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
