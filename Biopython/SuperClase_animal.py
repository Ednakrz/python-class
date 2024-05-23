'''
NOMBRE
Super clase animal
VERSION
  1.0 

AUTOR
 Edna Karen Rivera Zagal <ednakrz@lcg.unam.mx>

 SINOPSIS
    python .\SuperClase_animal.py

DESCRIPCION
   En este programa se creó una super clase llamada "animal", a partir de la cual se crearon otras dos clases llamadas "perro" y "gato", haciendo un override
   de la funcion "haz_ruido" de la super clase "animal"

CATEGORIA
    Super clase, clase.

OPCIONES 
    Este programa no cuenta con opciones por el memento para ingresar datos, por favor sigue el ejemplo de la forma para ejecutar el programa. 
USO 
Forma en la que se puede ejecutar el programa: 
  ejemplo: python .\SuperClase_animal.py

Ejemplo
  Linea de comando usada para el ejemplo: 
  python .\SuperClase_animal.py
  quieres que tu animalito grite?
  presióna uno para sí o cero para no
  1
'''
class animal (): 
    def __init__(self, Nombre, Edad): 
        self.Nombre = Nombre 
        self.Edad = Edad 
        self.respira = True 
        self.comer = True 
    def haz_ruido (self,ruido):
        if ruido == 1 : 
            print ("AAAAAAHHHH")
        else:
            print ("Es timida la creatura")

class perro(animal):
    def __init__(self, Nombre, Edad):
       super().__init__(Nombre,Edad) 

    def haz_ruido(self,ruido):
        if ruido !=0:
            print("Guau Guau:)")
        

class gato(animal):
    def __init__(self, Nombre, Edad):
        super().__init__(Nombre,Edad)
        self.usa_arenero = True
    def haz_ruido(self,ruido):
        if ruido !=0:
            print("Miau Miau:)")
    

if __name__ == "__main__":
    pajarito = animal ("Niña",8)
    print ("quieres que tu animalito hable?\npresióna uno para sí o cero para no")
    ruido = int(input())
    pajarito.haz_ruido(ruido) 
    print (pajarito.Nombre)
    perrito = perro("ares",3)
    perrito.haz_ruido(ruido)
    print(perrito.Nombre)
    gatito = gato("Senna",1)
    gatito.haz_ruido(ruido)
    print (gatito.Nombre)