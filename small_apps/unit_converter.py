# Fixes:
# Round values better
# Validate Input

# Length -----------------------------------------------
def get_millimeter(length, base_unit):
    length = float(length)
    if base_unit == "Millimeter":
        return length
    elif base_unit == "Centimeter":
        return length * 10
    elif base_unit == "Meter":
        return length * 1000
    elif base_unit == "Kilometer":
        return length * 1000000
    elif base_unit == "Inch":
        return length * 25.4
    elif base_unit == "Foot":
        return length * 304.8
    elif base_unit == "Yard":
        return length * 914.4
    elif base_unit == "Mile":
        return length * 1.609E+6
    else: raise ValueError(f"Unknown unit: {base_unit}")

def get_length(length, base_unit, end_unit):
    millimeter = float(get_millimeter(length, base_unit))
    if end_unit == "Millimeter":
        return millimeter
    elif end_unit == "Centimeter":
        return millimeter / 10
    elif end_unit == "Meter":
        return millimeter / 1000
    elif end_unit == "Kilometer":
        return millimeter / 1000000
    elif end_unit == "Inch":
        return millimeter / 25.4
    elif end_unit == "Foot":
        return millimeter / 304.8
    elif end_unit == "Yard":
        return millimeter / 914.4
    elif end_unit == "Mile":
        return millimeter / 1.609E+6
    else: raise ValueError(f"Unknown unit: {end_unit}")

# Weight -----------------------------------------------
def get_gram(weight, base_unit):
    weight = float(weight)
    if base_unit == "Gram":
        return float(weight)
    elif base_unit == "Milligram":
        return float(weight / 1000)
    elif base_unit == "Kilogram":
        return float(weight * 1000)
    elif base_unit == "Ounce":
        return float(weight * 28.3495)
    elif base_unit == "Pound":
        return float(weight * 453.592)
    else: raise ValueError(f"Unknown unit: {base_unit}")

def get_weight(weight, base_unit, end_unit):
    gram = float(get_gram(weight, base_unit))
    if end_unit == "Milligram":
        return gram * 1000
    elif end_unit == "Gram":
        return gram
    elif end_unit == "Kilogram":
        return gram / 1000
    elif end_unit == "Ounce":
        return gram / 28.3495
    elif end_unit == "Pound":
        return gram / 453.592
    else: raise ValueError(f"Unknown unit: {end_unit}")


# Temperature ---------------------------------------------
def get_celsius(temp, base_unit):
    temp = float(temp)
    if base_unit == "Celsius":
        return temp
    elif base_unit == "Fahrenheit":
        return (temp - 32) * 5/9
    elif base_unit == "Kelvin":
        return temp - 273.15
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


# App ------------------------------------------------------------

category_input = input("""1: Length
2: Weight
3: Temperature
Select which category you would like to convert: """)
startingQuantity = input("Select the quantity you would like to convert: ")

if category_input == "1":
    startingUnit = input("""Select which unit you would like to convert from:
Millimeter | Centimeter | Meter | Kilometer | Inch | Foot | Yard | Mile >> """).strip().capitalize()
    endingUnit = input("""Select which unit you would like to convert to:
Millimeter | Centimeter | Meter | Kilometer | Inch | Foot | Yard | Mile >> """).strip().capitalize()

    endingQuantity = get_length(startingQuantity, startingUnit, endingUnit)
    print(f"Your request: {startingQuantity} {startingUnit} = {endingQuantity} {endingUnit}")


elif category_input == "2":
    startingUnit = input("""Select which unit you would like to convert from:
Milligram | Gram | Kilogram | Ounce | Pound >> """).strip().capitalize()
    endingUnit = input("""Select which unit you would like to convert to:
Milligram | Gram | Kilogram | Ounce | Pound >> """).strip().capitalize()

    endingQuantity = get_weight(startingQuantity, startingUnit, endingUnit)
    print(f"Your request: {startingQuantity} {startingUnit} = {endingQuantity} {endingUnit}")

elif category_input == "3":
    startingUnit = input("""Select which unit you would like to convert from:
Celsius | Fahrenheit | Kelvin >> """).strip().capitalize()
    endingUnit = input("""Select which unit you would like to convert to:
Celsius | Fahrenheit | Kelvin >> """).strip().capitalize()

    endingQuantity = get_temperature(startingQuantity, startingUnit, endingUnit)
    print(f"Your request: {startingQuantity}° {startingUnit} = {endingQuantity}° {endingUnit}")

else: print("Invalid input")






