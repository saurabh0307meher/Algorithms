import numpy as np
import matplotlib.pyplot as plt
from statistics import mean 
from matplotlib import style
style.use('ggplot')
import pandas as pd

xs = np.array([1,2,3,4,5] , dtype = np.float64)
ys = np.array([5,4,6,5,6] , dtype = np.float64)

def best_fit_slope_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys))/
         ((mean(xs)*mean(xs))-mean(xs*ys)))
    
    b = mean(ys) - m*mean(xs)
    return m,b
          
m,b = best_fit_slope_intercept(xs,ys)

print(m,b) 
