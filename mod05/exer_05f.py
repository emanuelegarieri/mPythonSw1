import random

points = int(input("How many random points should be generated? "))

inside = 0

for _ in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        inside += 1

pi_approximation = 4 * inside / points

print("Approximation of pi:", pi_approximation)