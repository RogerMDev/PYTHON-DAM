import random
from random import randint


class Personaje:
    def __init__(self, nombre, salud, ataque, defensa):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.experiencia = 0

    def atacar(self, otro_personaje):
        dano = random.randint(0,self.ataque)
        print(f"{self.nombre} ataca a {otro_personaje.nombre} y causa {dano} de daño")
        otro_personaje.recibir_dano(dano)

    def recibir_dano(self,dano):
        self.salud -= max(0,dano - self.defensa)
        if self.salud < 0:
            self.salud = 0

    def esta_vivo(self):
        return self.salud > 0

    def estadistiques(self):
        print(f"El personaje {self.nombre} tiene {self.salud} salud, {self.ataque} ataque y {self.defensa} defensa ")

    def recalcular_ataque_defensa(self):
        if self.experiencia > 0:
            self.ataque = (1+(0.1 * self.experiencia)*self.ataque)
            self.defensa = (1+(0.1 * self.experiencia)*self.defensa)

class Juego:
    def __init__(self,personaje1,personaje2):
        self.personaje1 = personaje1
        self.personaje2 = personaje2

    def combate(self):
        self.personaje1.estadistiques()
        self.personaje2.estadistiques()
        while self.personaje1.esta_vivo() and self.personaje2.esta_vivo():
            print("Personatge 1 ataca a personaje 2")
            self.personaje1.atacar(self.personaje2)
            juego1.versus()
            print("Personatge 2 ataca a personatge 1")
            self.personaje2.atacar(self.personaje1)
            juego1.versus()

        if self.personaje1.esta_vivo():
            print(f"{self.personaje1.nombre} ha ganado")
            self.personaje1.experiencia += 1
            self.personaje1.recalcular_ataque_defensa()
            self.personaje1.estadistiques()
        else:
            print(f"{self.personaje2.nombre} ha ganado")
            self.personaje2.experiencia += 1
            self.personaje2.recalcular_ataque_defensa()
            self.personaje2.estadistiques()

    def versus(self):
        print(f"{self.personaje1.nombre} // {self.personaje2.nombre}")
        print(f"  {self.personaje1.salud} // {self.personaje2.salud}")


p1 = Personaje("Ignasi",100,100,2)
p2 = Personaje("Joan",100,80,3)

juego1 = Juego(p1,p2)
juego1.combate()









