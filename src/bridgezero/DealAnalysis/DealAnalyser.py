from bridgezero.Contract.ContractService import ContractService
from bridgezero.DealAnalysis.ProbabilityCalculator.ProbabilityCalculator import ProbabilityCalculator
from bridgezero.DealAnalysis.filters.DblRdbl import DblRdbl
from bridgezero.DealAnalysis.filters.Minimax import Minimax
from bridgezero.DealAnalysis.filters.SameResultForBothDeclarersInSide import SameResultForBothDeclarersInSide


class DealAnalyser:
    @staticmethod
    def analyseDeal(deal):
        tricksProbabilities = ProbabilityCalculator.calculateHandsTricksProbabilities(deal)

        contractsEvaluated = ContractService.evaluateContracts(
            ContractService.getAllContracts(
                vulnerable_NS=deal.get_side_ns_vulnerable(),
                vulnerable_EW=deal.get_side_ew_vulnerable()
            ),
            tricksProbabilities
        )

        contractsFiltered0 = {}

        for contractEv in contractsEvaluated:
            contractsFiltered0[contractEv['contract'].getHash()] = contractEv

        contractsFiltered1 = SameResultForBothDeclarersInSide.filter(contractsFiltered0)

        contractsFiltered2 = DblRdbl.filter(contractsFiltered1)

        minimax = Minimax.filter(contractsFiltered2)

        # analysis results
        deal.analysis = {
            "minimax_contract_NS": minimax['contract'].getHash(),
            "minimax_ev_NS": minimax['ev'],
            "tricks_probabilities_NS": tricksProbabilities
        }
