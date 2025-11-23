def bmi(weight, height, system="metric"):
    if system == "metric":
        bmi_value = weight / (height ** 2)
    elif system == "imperial":
        bmi_value = (weight / (height ** 2)) * 703
    else:
        return -1, None

    if bmi_value < 16:
        classification = "Severe Thinness"
    elif bmi_value < 17:
        classification = "Moderate Thinness"
    elif bmi_value < 18.5:
        classification = "Mild Thinness"
    elif bmi_value < 25:
        classification = "Normal"
    elif bmi_value < 30:
        classification = "Overweight"
    elif bmi_value < 35:
        classification = "Obese Class I"
    elif bmi_value < 40:
        classification = "Obese Class II"
    else:
        classification = "Obese Class III"

    return bmi_value, classification


b,c = bmi(80, 1.75, "metric")
print(f"{b:.2f} {c}")
b,c = bmi(98, 1.80, "metric")
print(f"{b:.2f} {c}")
b,c = bmi(176.37, 68.898, "imperial")
print(f"{b:.2f} {c}")
