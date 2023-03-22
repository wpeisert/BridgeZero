class TricksProbabilities:
    def __init__(self, probs):
        self.probs = probs

    def getProbabilities(self, declarer, color):
        return self.probs[declarer][color]
