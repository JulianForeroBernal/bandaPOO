from random import randint as rn
class Instrumento:
    def __init__(self,nombre):
        self.nombre=nombre
    def afinar (self):
        pass
    def tocar (self):
        pass

class Musico :
    def __init__(self,instrument,nombre_musico):
        self.instrumento=instrument
        self.nombre_musico=nombre_musico
    def afinar_instrumento(self):
        self.instrumento.afinar()
    def tocar_instrumetno (self):
        self.instrumento.tocar()

class Banda:
    def __init__(self,musicos):
        self.musicos=musicos
    def afinacion (self):
        pass