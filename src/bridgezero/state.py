class State:
    """
    This class keeps state
    """

    PROPERTIES = ['cards', 'bidding', 'we_vulnerable', 'they_vulnerable'];

    def __init__(self, **kwargs):

        #for prop in State.PROPERTIES:
        #    setattr(self, prop, None)
        self.cards = None
        self.bidding = None
        self.we_vulnerable = None
        self.they_vulnerable = None
        self.set(**kwargs)

    def set(self, **kwargs):
        for (i, v) in kwargs.items():
            if i in State.PROPERTIES:
                setattr(self, i, v)
            else:
                raise Exception("Bad property: {}. Should be one of: {}".format(i, State.PROPERTIES))

    def is_valid(self):
        raise NotImplementedError
