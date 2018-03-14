import numpy as np 


class GradientDescent():
	"""
	           Simple Implementation of Gradient Descent

	function:    Cost function
	derivatives: List of functions, that is the partial derivative of 
	             the cost function with respect to each variable.
	max_iter:    Maximum number of iterations of the algorithm.
	eta:         How big will be the step.
	[low, high): Range of initialization of each variables.
	eps:         Epsilon for stop the algorithm when the norm of the 
	             gradient be less than it.
	"""
	
	def __init__(self, function, derivatives, max_iter=10000, eta=0.2, low=-0.5, high=0.5, eps=1e-10):
		
		self.n_variables = len(derivatives)

		self.function = function
		self.derivatives = derivatives
		self.max_iter = max_iter
		self.eta = eta
		self.eps = eps

		self.gradient = np.zeros(self.n_variables)
		self.w = np.random.uniform(low, high, self.n_variables)


	def compute_gradient(self):

		for i in xrange(self.n_variables):
			self.gradient[i] = self.derivatives[i](self.w)


	def update_weights(self):

		self.w -= self.eta * self.gradient
		

	def evaluate(self):

		return self.function(self.w)


	def run(self):

		for i in xrange(self.max_iter):

			self.compute_gradient()
			self.update_weights()
			eva = self.evaluate()
			print('Iteration {}: {}'.format(i, eva))

			if np.linalg.norm(self.gradient) < self.eps:
				print('Converged before the maximum number of iterations.')
				print('Norm of gradient is smaller than epsilon.')				
				break

		print('Gradient: {}'.format(self.gradient))
		print('Weight:   {}'.format(self.w))


