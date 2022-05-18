import numpy as np
import matplotlib.pyplot as plt

def rand_gen(n=1000):
    return(np.random.randn(n))

def plot_rand(array):
    plt.figure()
    plt.hist(array, bins='auto')
    plt.xlabel('Value')
    plt.ylabel('Counts')
    plt.title('Gaussian Distribution Hist of %d Numbers'%len(array))
    plt.show()
    plt.savefig('../figures/gaussian_hist.pdf')
    return

def main():
    array = rand_gen()
    plot_rand(array)

if __name__ == "__main__":
    main() 
