import numpy as np
from numpy.random import RandomState
prng = RandomState(1234567890)

class Forward:
  def __init__(self, shape, activations):
    self.shape = shape
    self.activations = [np.vectorize(a) for a in activations]
    self.weights = [np.array([prng.uniform(-1, 1, shape[i + 1]) for n in range(shape[i])]) for i in range(len(shape)) if i < len(shape) - 1]
    self.biases = [prng.uniform(-1, 1, shape[i]) for i in range(len(shape))]

  def predict(self, X):
    predictions = []
    for x in X:
      for i in range(len(self.shape)):
        x = np.add(x, self.biases[i])
        x = self.activations[i](x)
        if i < len(self.shape) - 1:
          x = np.dot(x, self.weights[i])
      predictions.append(x)
    return predictions

# For testing purposes
"""
# Defining some activation functions
def sigmoid(x, prime=False):
  if not prime:
    if x < 0:
      return 1/(1+np.exp(x))
    else:
      return 1/(1+np.exp(-x))
  else:
    return sigmoid(x)*(1-sigmoid(x))
  
def ReLu(x, prime=False):
  if not prime:
    return max(0,x)
  else:
    return max(max(0, x),1)

model = Forward(shape=[3,3,3],activations=[ReLu,ReLu,sigmoid])
predictions = model.predict([[1,1,0],[1,0,1],[0,0,0]])
print(predictions)
"""