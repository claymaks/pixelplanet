import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 11)
xU, xL = x + 0.5, x - 0.5 
prob = ss.norm.cdf(xU, scale = 3) - ss.norm.cdf(xL, scale = 3)
prob = prob / prob.sum() #normalize the probabilities so their sum is 1
nums = np.random.choice(x, size = 10000, p = prob)
accu = 0
for i in nums:
    accu+=i
print(float(accu/size))
