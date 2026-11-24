celsius = int(input())
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

if kelvin >= 0:
    print("Fahrenheit =", fahrenheit)
    print("Kelvin =", kelvin)
else:
    print("Invalid Temperature")