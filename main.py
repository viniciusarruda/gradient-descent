from gradient import GradientDescent


def univariate(x):
	return (x - 1.0)**2 + 1.0

def derivative_univariate(x):
	return 2.0 * (x - 1.0)


def multivariate(x):
	return 3.0 * x[0]**2 + 3.0 * x[0] * x[1] + 2.0 * x[1]**2 + x[0] + x[1]

def derivative_multivariate_0(x):
	return 6.0 * x[0] + 3.0 * x[1] + 1.0

def derivative_multivariate_1(x):
	return 3.0 * x[0] + 4.0 * x[1] + 1.0


def main():

	# Run with the univariate example
	gd = GradientDescent(univariate, [derivative_univariate])

	# Run with the multivariate example
	gd = GradientDescent(multivariate, [derivative_multivariate_0, derivative_multivariate_1])

	gd.run()


if __name__ == '__main__':
	main()

