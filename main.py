import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


data = pd.read_csv('data1.csv')
X = np.array(data.iloc[:, 0])
Y = np.array(data.iloc[:, 1])

# plt.scatter(X, Y) 
# plt.plot()  # regression line
# plt.show()

tetha_0 = 0
tetha_1 = 0

alpha = 0.000063
step_count = 1000

n = len(X)

for i in range(step_count):
    h_tetha = tetha_0 + tetha_1 * X

    tetha_1_D = (1/n) * np.sum(X * (h_tetha - Y))
    tetha_0_D = (1/n) * np.sum(h_tetha - Y)

    tetha_1 = tetha_1 - (alpha * tetha_1_D)
    tetha_0 = tetha_0 - (alpha * tetha_0_D)
    # print(tetha_0, tetha_1)

print(f"Tetha 0: {tetha_0}, Tetha 1: {tetha_1}")

h_tetha = tetha_0 + tetha_1 * X
# print(h_tetha)
# print([min(X), max(X)], [min(h_tetha), max(h_tetha)])

plt.scatter(X, Y) 
plt.plot([min(X), max(X)], [min(h_tetha), max(h_tetha)], color='red')  # regression line
plt.show()
