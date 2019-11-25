import numpy as np
import features.algorithms.models as models


class SimObj:
    """ This class acts as a base class of all simulated objects """

	""" ID is used to identify an object numerically"""
    _id = 0

    def impress(self):
        """ Impress is intended to be defined in child classes """
        raise NotImplementedError

    def express(self):
        """ Express is intended to be defined in child classes """
        raise NotImplementedError


class Blob(SimObj):

	_id = 1

	def __init__(self, position):
		"""
		input: [obj_in_sight, is_touching_obj, relative_obj_direction]
		output: [angle, accel]
		"""
		self.brain = models.Forward(shape=[3, 4, 2], activations=[lambda x: x] * 3)
		self.input = np.zeros(3)
		self.output = np.zeros(2)
		"""
		position: [x, y]
		momentum: [x, y]
		angle: θ
		accel: a
		"""
		self.radius = 10
        self.position = np.array(position)
        self.momentum = np.zeros(2)
        self.angle = 0
        self.accel = 0


    def impress(self):
    	self.input = np.array(3)
        self.output = self.brain.predict([self.input])[0]

    def express(self):
        self.angle = self.output[0]
        self.accel = self.output[0]
        self.momentum += [self.accel * np.sin(self.angle), self.accel * np.cos(self.angle)]
        self.position += self.momentum


class Ball(SimObj):

	_id = 2

	def __init__(self, position):
		self.radius = 10
		self.position = np.array(position)
		self.momentum = np.zeros(2)

	def impress(self):
    	pass

    def express(self):
    	pass

class Goal(SimObj):

	_id = 3

	def __init__(self, position):
		self.position = position
		self.size = 500

	def impress(self):
    	pass

    def express(self):
    	pass

class Wall(SimObj):

	_id = 4

	def __init__(self, position, angle):
		self.position = position
		self.size = 500

	def impress(self):
    	pass

    def express(self):
    	pass

# For testing purposes
"""
blob = Blob()
blob.input = [0] * 4
blob.update()
print(blob.output)

"""
