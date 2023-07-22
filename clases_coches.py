
class Vehiculo:
    def __init__(self, color, ruedas, puertas) -> None:
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
            return f"es de color {self.color}, tiene {self.ruedas} ruedas, {self.puertas} puertas"

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}, alcanza {self.velocidad} km/hora de velocidad, y tiene {self.cilindrada} L de cilindrada."


mini = Coche("gris", 4, 3, 180, 1.5)
print("El mini", mini)