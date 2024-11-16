import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Example data
data = np.random.normal(0, 1, 1000)

# Applying Sturges rule
n = len(data)
k = int(1 + np.log2(n)) # or k = int(1+3.322*np.log(n))

# Create a histogram
plt.figure(figsize=(8,6))
plt.hist(data, bins=k, edgecolor='black', color='skyblue')
plt.title("Data Values", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.show()

print(f"Number of bins based on Sturges Rule: {k}")


