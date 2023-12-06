from numba import jit, cuda
import numpy as np

import pandas as pd
# to measure exec time
from timeit import default_timer as timer   
  
# normal function to run on cpu

def alpha_MoM(df):
    return np.sqrt(np.sum(np.power(df, 2))/len(df) -np.power(np.sum(df)/len(df), 2) )     

# function optimized to run on gpu 
@jit(target_backend='cuda')                         
def alpha_MoM2(df):
    return np.sqrt(np.sum(np.power(df, 2))/len(df) -np.power(np.sum(df)/len(df), 2) )

if __name__=="__main__":
    df = np.array(pd.read_csv('Вдовин Игорь.csv')['sample'])
    n = 10000000                            
    a = np.ones(n, dtype = np.float64)
      
    # start = timer()
    # a2 = [alpha_MoM(df[:i]) for i in range(999999, 100000, -100)]
    # print("without GPU:", timer()-start)    
    
    start = timer()
    a1 = [alpha_MoM2(df[:i]) for i in range(999999, 100000, -100)]
    print("with GPU:", timer()-start)