import numpy as np
from . import intelligence

class gesi(intelligence.sw):
	def __init__(self, n, function, lb, ub, dimension, iteration):
		super(gesi, self).__init__()
		
		# initial positions
		self._agents = np.random.uniform(lb, ub, (n, dimension))
		self._points(self._agents)

		# initial evaluation
		Pbest = self._agents[np.array([function(x)for x in self._agents]).argmin()]
		Gbest = Pbest

		# auxilary declarations
		velocity = np.zeros((n, dimension))
		nest = 100
		self._nests = np.random.uniform(lb, ub, (nest, dimension))

		# main loop
		for t in range(iteration):
			# update variants
			# 1
			# self._velocity(Pbest, Gbest, n, dimension, velocity)
			
			# 2
			self._Levyfly(Pbest, n, dimension)
			
			# swap variants
			# 1
			# swap = None

			# 2
			swap = 1
			for i in self._agents: 
				val = np.random.randint(0, nest - 1)
				if function(i) < function(self._nests[val]):
					self._nests[val] = i

			# selection variants
			# 1
			# selection = None

			# 2
			# drop_worst = 1
			# self._drop_worst_chance(nest, lb, ub, dimension, function)

			# 3
			swap = 1
			drop_worst = 1
			self._drop_worst_chance(nest, lb, ub, dimension, function)
			self._ordered_swap(n, nest, function)

			# 4
			# swap = 1
			# self._ordered_swap(n, nest, function)

			# clip
			self._agents = np.clip(self._agents, lb, ub)
			self._nests = np.clip(self._nests, lb, ub)
			self._points(self._agents)


			# choose best
			if swap:
				Pbest = self._nests[np.array([function(x) for x in self._nests]).argmin()]
			else:
				Pbest = self._agents[np.array([function(x) for x in self._agents]).argmin()]

			# update best
			if function(Pbest) < function(Gbest):
				Gbest = Pbest

			# result
			self._set_Gbest(Gbest)
