#banda
#julian foero
#28/02/2024

from random import randint as rn
from random import choice
class Instrumento:
    def afinar (self):
        pass
    def tocar (self):
        pass
    def mostrar(self):
        return "instrumento " + str(type(self)).split(".")[-1][:-2]

class Guitarra(Instrumento):
    def afinar(self):
        return("afinando guitarra ")
    def tocar(self):
        return("tocando  guitarra")
class piano (Instrumento):
    def afinar(self):
        return("afinando piano ")
    def tocar(self):
        return("tocando piano")
class saxofon (Instrumento):
    def afinar(self):
        return("afinando saxofon ")
    def tocar(self):
        return("tocando saxofon")
class trompeta (Instrumento):
    def afinar(self):
        return("afinando trompeta ")
    def tocar(self):
        return("tocando tropeta")
class ukelele (Instrumento):
    def afinar(self):
        return("afinando ukelele ")
    def tocar(self):
        return("tocando ukelele")
class bajo (Instrumento):
    def afinar(self):
        return("afinando bajo ")
    def tocar(self):
        return("tocando bajo")
class violin (Instrumento):
    def afinar(self):
        return("afinando violin ")
    def tocar(self):
        return("tocando violin")
class acordeon (Instrumento):
    def afinar(self):
        return("afinando acordeon ")
    def tocar(self):
        return("tocando acordeon")
class flauta (Instrumento):
    def afinar(self):
        return("afinando flauta ")
    def tocar(self):
        return("tocando flauta")
class banjo (Instrumento):
    def afinar(self):
        return("afinando banjo ")
    def tocar(self):
        return("tocando banjo")

class Musico :
    def __init__(self,nombre):
        self.nombre=nombre
        self.instrumento=None
    def asignar_instrumento(self,instrumento):
        self.instrumento = instrumento
    def afinar_instrumento(self):
        return self.instrumento.afinar()
    def tocar_instrumento (self):
        return self.instrumento.tocar()

class Banda:
    def __init__(self):
        self.musicos=[]
        self.instrumentos=[Guitarra(),piano(),saxofon(),trompeta(),ukelele(),bajo(),violin(),acordeon(),flauta(),banjo()]
        self.amigos=["juan","carlos","pedro","miguel","camilo","dante","lucas","pepe","alejandro","beto"]
    def crear_banda(self,cantidad_musicos):
        for i in range(cantidad_musicos):
            self.musicos.append(Musico(choice(self.amigos)))
            self.musicos[-1].asignar_instrumento(choice(self.instrumentos))
    def mostrar_banda(self):
        for m in self.musicos:
            print(m.nombre)
            print((m.instrumento.mostrar()))
    def afinar_banda(self):
        for j in self.musicos:
            print(j.afinar_instrumento())
    def tocar_banda(self):
        for m in self.musicos:
            print(m.tocar_instrumento())
    


if __name__ == "__main__":
    b = Banda()
    b.crear_banda(2)
    b.mostrar_banda()
    print("afina la banda")
    b.afinar_banda()
    print("toca la banda")
    b.tocar_banda()