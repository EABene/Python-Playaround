""" Length: *millimeter, centimeter, meter, kilometer, inch, foot, yard, mile.

Weight: milligram, *gram, kilogram, ounce, pound.

Temperature: *Celsius, Fahrenheit, Kelvin.

Enter length to convert:| Unit to convert from | Unit to convert to:
"""
# Weight ----------------------------------
def get_gram(weight, base_unit):
    if base_unit == "gram":
        return float(weight)
    elif base_unit == "milligram":
        return float(weight / 1000)
    elif base_unit == "kilogram":
        return float(weight * 1000)
    elif base_unit == "ounce":
        return float(weight * 28.3495)
    elif base_unit == "pound":
        return float(weight * 453.592)
    else: raise ValueError(f"Unknown unit: {base_unit}")

def get_weight(weight, base_unit, end_unit):
    gram = float(get_gram(weight, base_unit))
    if end_unit == "milligram":
        return gram * 1000





# Temperature -------------------------------
def get_celsius(temp, base_unit):
    if base_unit == "Celsius":
        return float(temp)
    elif base_unit == "Fahrenheit":
        return (float(temp) - 32) * 5/9
    elif base_unit == "Kelvin":
        return float(temp) - 273.15
    else: raise ValueError(f"Unknown unit: {base_unit}")

def get_temperature(temp, base_unit, end_unit):
    celsius = float(get_celsius(temp, base_unit))
    if end_unit == "Celsius":
        return celsius
    elif end_unit == "Fahrenheit":
        return (celsius * 9 / 5) + 32
    elif end_unit == "Kelvin":
        return celsius + 273.15
    else: raise ValueError(f"Unknown unit: {end_unit}")
# ------------------------------------------------------------



category_key = {
    1: "Length",
    2: "Weight",
    3: "Temperature"
}

category_input = input("""Select which category you would like to convert: 
                        1: Length
                        2: Weight
                        3: Temperature """)

startingQuantity = input("Select the quantity you would like to convert: ")

startingUnit = input("Select which unit you would like to convert from: ")

endingUnit = input("Select which unit you would like to convert to: ")

endingQuantity = get_temperature(startingQuantity, startingUnit, endingUnit)
print(f"Your request: {startingQuantity} {startingUnit} = {endingQuantity} {endingUnit}")






