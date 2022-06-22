class Alumno():
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def aprobado(self):
        aprobo=""
        if self.nota<6:
            aprobo="no "
        print(self.nombre, aprobo+"ha aprobado")


Alumnos = [Alumno("Juan Martinez",8), Alumno("Daniel Gutierres",4)]

for x in Alumnos:
    x.imprimir()
    x.aprobado()
    print()
