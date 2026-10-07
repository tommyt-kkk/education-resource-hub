import numpy as np
import matplotlib.pyplot as plt

N_values = [int(10 ** (2 + 4 * i / 24)) for i in range(25)]
errors = []

for N in N_values:

    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    inside_circle = x**2 + y**2 <= 1
    inside_count = np.sum(inside_circle)
    pi_estimate = 4 * inside_count / N
    error = abs(pi_estimate - np.pi)
    errors.append(error)

plt.plot(N_values, errors, marker="o")
plt.xscale("log")
plt.grid(True)
plt.show()
