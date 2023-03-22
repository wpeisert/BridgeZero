from bridgezero import dds
from bridgezero.DealAnalysis.ProbabilityCalculator.TricksProbabilities import TricksProbabilities


class ProbabilityCalculator:
    @staticmethod
    def calculateHandsTricksProbabilities(deal):
        # TODO rename class - this is not about probabilities
        pbn = deal.get_as_PBN()
        dd_results = dds.run_dds([deal])
        return TricksProbabilities(dd_results[0])
