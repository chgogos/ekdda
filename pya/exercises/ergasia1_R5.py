import math


def distance(theta, v):
    g = 9.81
    theta_rad = math.radians(theta)

    v_x = v * math.cos(theta_rad)
    v_y = v * math.sin(theta_rad)

    T = 2 * v_y / g
    R = v_x * T

    return R


theta = float(input("Δώσε τη γωνία εκτόξευσης (μοίρες): "))
v = float(input("Δώσε την αρχική ταχύτητα (m/s): "))

R = distance(theta, v)
print(f"Η οριζόντια απόσταση που διανύει το βλήμα είναι {R:.2f} m.")

# Extra ερώτημα
max_R = -1.0
best_theta = None

for angle in range(1, 90):  # 1° έως 89°
    current_R = distance(angle, v)
    if current_R > max_R:
        max_R = current_R
        best_theta = angle

print(
    f"Η μέγιστη απόσταση είναι {max_R:.2f} m και επιτυγχάνεται για γωνία εκτόξευσης {best_theta}°."
)
