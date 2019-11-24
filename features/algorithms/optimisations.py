import random

def breed(p1,p2):
	len1, len2 = len(p1),len(p2)
	if len1 != len2:
		raise ValueError(f"The two parts must be of same lengths\nlen(p1):{len1}\nlen(p2):{len2}")
	symbols = [1,2]
	random.shuffle(symbols)
	testament = [symbols[0] if i % 2 == 0 else symbols[1] for i in range(len1)]
	random.shuffle(testament)
	return [p1[i] if s == 1 else p2[i] for i, s in enumerate(testament)]

def mutate(p, force=0.5, rate=0.5):
	if type(rate) not in [int, float] or rate > 1 or rate < 0:
		raise ValueError(f"The rate is a probability and must therefore be a number between 0 and 1\nrate:{rate}")
	if type(force) not in [int, float]:
		raise ValueError(f"The force is a measurement and must therefore be a number\nforce:{force}")
	return [m if random.random() > rate else m+random.random()*force for m in p]

# For testing purposes
"""
p1 = [1,2,3,4,5,6,7,8,9,10]
p2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
p3 = breed(p1,p2)
print(p3)
p3 = mutate(p3)
print(p3)

"""