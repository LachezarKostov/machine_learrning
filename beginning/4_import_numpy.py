import numpy as np

data = list(map(float, input().split(' ')))

print(f"""
mean = {np.mean(data)}
median = {np.median(data)}
50% = {np.percentile(data, 50)}
25% = {np.percentile(data, 25)}
75% = {np.percentile(data, 75)}
standard deviation = {np.std(data)} 
variance = {np.var(data)}
""")

# 15 16 18 19 22 24 29 30 34