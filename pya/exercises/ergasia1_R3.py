def box_volume_surface(l, w, h):
    V = l * w * h
    S = 2 * (l*w + l*h + w*h)
    return V, S

count = 0

for l in range(1, 101):
    for w in range(1, 101):
        for h in range(1, 101):
            V, S = box_volume_surface(l, w, h)
            if 2<= V / S <= 3:
                count += 1

print("Πλήθος κουτιών με 2<= V/S <= 3 :", count)
