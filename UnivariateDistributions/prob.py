# Import necessary packages
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

# Sample data provided in lesson
sample_data = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

# Set seed for randomly generated values
np.random.seed(12345)

# Randomly generate 1000 samples for a standard normal and uniform distributions
random_normal = np.random.normal(size = 1000)
random_uniform = np.random.uniform(size = 1000)


# Box plots for each of the three data sets
plt.figure()
box_sample = plt.boxplot(sample_data)
plt.savefig("box_sample.png")

plt.figure()
box_normal = plt.boxplot(random_normal)
plt.savefig("box_normal.png")

plt.figure()
box_uniform = plt.boxplot(random_uniform)
plt.savefig("box_uniform.png")


# Histograms for each of the three data sets
plt.figure()
hist_sample = plt.hist(sample_data)
plt.savefig("hist_sample.png")

plt.figure()
hist_normal = plt.hist(random_normal)
plt.savefig("hist_normal.png")

plt.figure()
hist_uniform = plt.hist(random_uniform)
plt.savefig("hist_uniform.png")


# QQ Plots for each of the three data sets
plt.figure()
qq_sample = stats.probplot(sample_data, dist = "norm", plot = plt)
plt.savefig("qq_sample.png")

plt.figure()
qq_normal = stats.probplot(random_normal, dist = "norm", plot = plt)
plt.savefig("qq_normal.png")

plt.figure()
qq_uniform = stats.probplot(random_uniform, dist = "norm", plot = plt)
plt.savefig("qq_uniform.png")

