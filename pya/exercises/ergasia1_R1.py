import math


def distance_to_center(x, y):
    return math.sqrt(x * x + y * y)


distances = []
points = []
for i in range(1, 4):
    raw = input(f"Δώσε x και y για τη {i}η βολή: ").strip()
    x_str, y_str = raw.split()
    x = float(x_str)
    y = float(y_str)
    d = distance_to_center(x, y)
    distances.append(d)
    points.append((x, y))

min_dist = min(distances)
best_index = distances.index(min_dist)
shot_number = best_index + 1

# Θεωρούμε Bulls Eye αν η απόσταση είναι πρακτικώς μηδέν
EPS = 1e-12
if min_dist <= EPS:
    print(f"Bulls Eye στην {shot_number}η βολή!")
else:
    print(
        f"Η καλύτερη βολή ήταν η {shot_number}η με απόσταση από το στόχο {min_dist:.4f}"
    )
