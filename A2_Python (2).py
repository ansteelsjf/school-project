import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.misc import derivative

def f(x):
    return stats.norm.pdf(x, loc=mean, scale=std)

x = np.random.normal(0, 1, 10000)
mean = x.mean()
std = x.std(ddof=1)
x = np.arange(-5, 5, 0.01)
y = stats.norm.pdf(x, loc=mean, scale=std)
plt.plot(x, y)
d1=derivative(f, x, dx=1e-6)
plt.plot(x, d1)
d2=derivative(f, x,n=2, dx=1e-6)
plt.plot(x, d2)
plt.show()