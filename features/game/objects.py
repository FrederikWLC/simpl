import features.algorithms.models as models


class SimObj:
    """ This class acts as a base class of all simulated objects """

    def update(self):
        """ Update is intended to be defined in child classes """
        raise NotImplementedError


class Blob(SimObj):
    def __init__(self):
        self.brain = models.Forward(shape=[4, 4, 4], activations=[lambda x: x] * 3)
        self.input = None
        self.output = None

    def update(self):
        self.output = self.brain.predict([self.input])


# For testing purposes
"""
blob = Blob()
blob.input = [0] * 4
blob.update()
print(blob.output)

"""
