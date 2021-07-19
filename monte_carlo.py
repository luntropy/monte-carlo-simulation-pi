import numpy as np

radius = 1
total_dots = 100000
inner_dots = 0

# Using loop
# for dot in range(total_dots):
#     x = np.random.uniform(0, radius)
#     y = np.random.uniform(0, radius)
#
#     distance = np.sqrt(x**2 + y**2)
#     if distance <= radius:
#         inner_dots += 1
#
# print(4 * inner_dots / total_dots)

x = np.random.rand(1, total_dots)
y = np.random.rand(1, total_dots)

compare = (np.sqrt(x**2 + y**2) <= np.ones(total_dots))[0]
count_true = np.bincount(compare)[1]

print(4 * count_true / len(compare))
