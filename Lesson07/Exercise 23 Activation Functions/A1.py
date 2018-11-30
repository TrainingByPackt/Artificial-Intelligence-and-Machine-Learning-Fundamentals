def get_y( f, x3 ):
return f(2*1+0.5*2+1.5*x3)

import numpy as np
def sigmoid(x):
return 1 / (1 + np.e ** (-x))
def tanh(x):
return 2 / (1 + np.e ** (-2*x)) - 1
def relu(x):
return 0 if x < 0 else x

get_y( sigmoid, -2 )
#The output is 0.5
get_y(sigmoid, -1)
#The output is 0.8175744761936437
get_y(sigmoid, 0)
#The output is 0.9525741268224331
get_y(sigmoid, 1)
#The output is 0.9890130573694068
get_y(sigmoid, 2)
#The output is 0.9975273768433653

get_y(tanh, -2)
#The output is 0.0
get_y(tanh, -1)
#The output is 0.9051482536448663
get_y(tanh, 0)
#The output is 0.9950547536867307
get_y(tanh, 1)
#The output is 0.9997532108480274
get_y(tanh, 2)
#The output is 0.9999877116507956

get_y(relu,-2)
The output is 0.0
get_y(relu,-1)
#The output is 1.5
get_y(relu,0)
#The output is 3.0
get_y(relu,1)
#The output is 4.5
get_y(relu,2)
#The output is 6.0
