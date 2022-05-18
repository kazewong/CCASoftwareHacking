import numpy as np
import matplotlib.pyplot as plt

n = 1000
gaussian_rand = np.random.randn(n)

plt.figure()
plt.hist(gaussian_rand, bins='auto')
plt.xlabel('Value')
plt.ylabel('Counts')
plt.title('Gaussian Distribution Hist of %d Numbers'%n)
plt.show()
plt.savefig('../figures/gaussian_hist.pdf')
