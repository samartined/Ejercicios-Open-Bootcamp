
class Alumno:
    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = nota
        # float(self.nota)
        
    def __str__(self) -> str:
        return f"{self.nombre}, {self.nota}"

    def aprobado(self):
       if self.nota >= 5:
            return f"Aprobado"
       else:
            return f"No aprobado"

    
alumno1 = Alumno("Juan", 5)
alumno2 = Alumno("Fran", 4.99)

print(alumno1.nombre,", nota: ", alumno1.nota,",", alumno1.aprobado())
print(alumno2.nombre,", nota: ", alumno2.nota,",", alumno2.aprobado())