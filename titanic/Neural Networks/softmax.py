import numpy as np
def softmax(L):
	expL =np.exp(L)
	sumExpL =sum(expL)
	result =[]
	for i in expL:
		result.append(i*1.0/sumExpL)
	return result

# The function np.divide can also be used here, as follows:
# def softmax(L):
#	expL =np.exp(L)
#	return np.divide(expL, expL.sum())

# Trying for L=[5,6,7].
# The correct answer is
# [0.09003057317038046, 0.24472847105479764, 0.6652409557748219]
# And your code returned
# [0.09003057317038046, 0.24472847105479764, 0.6652409557748219]

if __name__ == '__main__':
	L=[5,6,7]
	print(softmax(L))
