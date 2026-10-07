import random
import math
import matplotlib.pyplot as plt

def estimate_pi(N):
    inside_count = 0
    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_count += 1
    return 4 * inside_count / N

sample_sizes = [int(10 ** (2 + 4 * i / 24)) for i in range(25)]

estimates = []
errors = []


for N in sample_sizes:
    pi_hat = estimate_pi(N)
    error = abs(pi_hat - math.pi)

    estimates.append(pi_hat)
    errors.append(error)

plt.plot(sample_sizes, errors, marker="o")

plt.xscale("log")
plt.xlabel("Sample Size N (log)")
plt.ylabel("Absolute Error")
plt.title("Error for Pi")
plt.grid(True, linestyle="--", alpha=0.5)

plt.show()
