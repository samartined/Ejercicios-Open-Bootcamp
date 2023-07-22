
def bisiestos(year):
    if year % 4 == 0:
        return f"{year} es bisiesto."
    return f"{year} no es bisiesto."


year = int(input("Introduzca un año: "))

print(bisiestos(year))