#Estas desarrollando un sistema  para un sistema para una biblioteca que necesita gestionar
# informacion sobre estudiantes libros y prestamos de libros a estudiantes.
#Requisitos:
#1 Clase Persona:
# * Debe tener atributos como nombre y edad.
# * Debe tener un metodo para mostrar la informacion de la persona.

class Persona():
    def __init__(self, dni: int, nombre: str, edad: int):
        self.dni=dni
        self.nombre=nombre
        self.edad=edad
    def mostrar_persona(self):
        print(f"NOMBRE: {self.nombre}\n"
              f"DNI: {self.dni}\n"
              f"EDAD: {self.edad}")

#2 Clase Estudiante: 
# * Debe heredar de la Clase Persona.
# * Debe tener un atributo adicional grado.
# * Debe tener un metodo mostrar que incluya  la informacion de la persona y el grado.

class Estudiante(Persona):
    def __init__(self, dni, nombre, edad, grado):
        super().__init__(dni, nombre, edad)
        self.grado=grado

    def mostrar_estudiante(self):
        print(f"NOMBRE: {self.nombre}\n"
              f"DNI: {self.dni}\n"
              f"EDAD: {self.edad}\n"
              f"GRADO: {self.grado}")
#3 Clase Libro:
# * Debe tener atributos  como titulo y autor.
# * Debe tener un metodo para mostrar la informacion del libro.

class Libro():
    def __init__(self, titulo, autor):
        self.titulo=titulo
        self.autor=autor

    def mostrar_libro(self):
        print(f"LIBRO: {self.titulo}\n"
              f"AUTOR: {self.autor}")

#4 Clase Prestamo:
# * Debe tener atributos estudiantes, libros y fecha_prestamo.
# * Debe tener un metodo para mostrar la informacion del prestamo,
# incluyendo el nombre del estudiante y el titulo del libro.
class Prestamo():
    def __init__(self, estudiante, fecha):
        self.estudiante=estudiante
        self.libros=[]
        self.fecha=fecha
        
    def añadir_libro(self, titulos):
        self.libros.append(titulos)

    def mostrar_prestamos(self):
        for i, libro in enumerate(self.libros):
            print(f"{i+1}) LIBRO: {libro.titulo}")
        print(f"ESTUDIANTE: {self.estudiante.nombre}\n"
                f"FECHA: {self.fecha}")


class Estudiante(Persona):
    def __init__(self, dni, nombre, edad, grado):
        super().__init__(dni, nombre, edad)
        self.grado=grado
    def mostrar_persona(self):
        print(f"NOMBRE: {self.nombre}\n"
              f"GRADO: {self.grado}")


alumno1=Estudiante(39398884, "Omar", 29, "5to")
libro1=Libro("Programacion para no morir", "X")
libro2=Libro("X", "x")

prestamo1=Prestamo(alumno1, "16/05/2024")
prestamo1.añadir_libro(libro1)
prestamo1.añadir_libro(libro2)
prestamo1.mostrar_prestamos()
