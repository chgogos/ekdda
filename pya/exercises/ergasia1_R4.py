n = int(input("Πόσες τιμές θα εισαχθούν; "))

prev = None
total = 0
count = 0
minimum = None
maximum = None

increasing = True
decreasing = True
equal_pair = False

for i in range(1, n + 1):
    value = float(input(f"Δώσε τιμή {i}: "))

    total += value
    count += 1

    if minimum is None or value < minimum:
        minimum = value
    if maximum is None or value > maximum:
        maximum = value

    if prev is not None:
        if value < prev:
            increasing = False
        if value > prev:
            decreasing = False
        if value == prev:
            equal_pair = True

    prev = value

avg = total / count

print("\nΜέγιστη τιμή:", maximum)
print("Ελάχιστη τιμή:", minimum)
print("Μέση τιμή:", avg)

if increasing:
    print("Οι τιμές ήταν διατεταγμένες σε αύξουσα σειρά.")
elif decreasing:
    print("Οι τιμές ήταν διατεταγμένες σε φθίνουσα σειρά.")
else:
    print("Οι τιμές δεν ήταν διατεταγμένες.")

if equal_pair:
    print("Υπήρξαν δύο συνεχόμενες ίσες τιμές.")
else:
    print("Δεν υπήρξαν συνεχόμενες ίσες τιμές.")