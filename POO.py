class animal (): 
    def __init__(self, Nombre, Edad): 
        self.Nombre = Nombre 
        self.Edad = Edad 
        self.respira = True 
        self.comer = True 
    def haz_ruido (self,ruido):
        if ruido == "1" : 
            print ("AAAAAAHHHH")
        else:
            print ("Es timida la creatura")

class perro(animal):
    def __init__(self, Nombre, Edad):
       super().__init__(Nombre,Edad) 

    def haz_ruido(self,ruido):
        print("Guau Guau:)")
        

class gato(animal):
    def __init__(self, Nombre, Edad):
        super().__init__(Nombre,Edad)
        self.usa_arenero = True
    def haz_ruido(self,ruido):
        print("Miau Miau:)")

if __name__ == "__main__":
    pajarito = animal ("Niña",8)
    print ("quieres que tu animalito grite?\npresióna uno para sí o cero para no")
    ruido = input()
    pajarito.haz_ruido(ruido) 
    print (pajarito.Nombre)
    perrito = perro("ares",3)
    perrito.haz_ruido(ruido)
    print(perrito.Nombre)
    gatito = gato("Senna",1)
    gatito.haz_ruido(ruido)
    print (gatito.Nombre)
