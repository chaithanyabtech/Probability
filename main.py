import scipy.stats as stats

# Define the parameters
n = 6
p = 2/3

# Calculate mean and standard deviation
mean = n * p
std_deviation = (n * p * (1 - p)) ** 0.5

# Calculate the z-score for x = 3.5 (continuity correction)
x = 3.5
z = (x - mean) / std_deviation

# Use the cumulative distribution function (CDF) to find P(X < 4)
probability_less_than_4 = stats.norm.cdf(z)

# Calculate P(X ≥ 4)
probability_at_least_4 = 1 - probability_less_than_4

print(f"Probability of at least 4 successes: {probability_at_least_4:.4f}")

