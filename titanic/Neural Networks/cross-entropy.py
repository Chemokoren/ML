import numpy as np
def cross_entropy(Y,P):
	Y = np.float_(Y)
	P = np.float_(P)
	return -np.sum(Y * np.log(P)+(1-Y) * np.log(1-P))

if __name__ == '__main__':
	new_y=[1,0,1,1]
	new_p=[0.4,0.6,0.1,0.5]

	print(cross_entropy(new_y,new_p))


# output
#4.828313737302301