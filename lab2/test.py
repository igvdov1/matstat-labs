import numpy as np
import cmath
def f(re, im):
    temp = complex(re, im)
    temp1 = complex(0, 1)
    return complex((temp+temp1)/(1+temp1*temp))

if __name__ == '__main__':
    u = np.linspace(-1, 1, 1000)
    v = np.linspace(-1, 1, 1000)
    for i, j in zip(u,v):
        print(f(i, j))