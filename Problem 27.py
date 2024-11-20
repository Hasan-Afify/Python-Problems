def celsius_to_fahrenheit(temp):
            return (temp * 9/5) + 32
def fahrenheit_to_celsius(temp):
            return (temp - 32) * 5/9
def celsius_to_kelvin(temp):
            return temp + 273.15
def kelvin_to_celsius(temp):
            return temp - 273.15
def Converting_Temperature(x,From,To):
    if From=="celsius" and To=="fahrenheit":
        return celsius_to_fahrenheit(x)
    elif From=="fahrenheit" and To=="celsius":
        return fahrenheit_to_celsius(x)
    elif From=="celsius" and To=="kelvin":
        return celsius_to_kelvin(x)
    elif From=="kelvin" and To=="celsius":
        return kelvin_to_celsius(x)

print(Converting_Temperature(37,"kelvin","celsius"))

