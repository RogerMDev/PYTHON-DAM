
class ColaLifo:
    def __init__(self):
        """
        Constructor de la classe.
        Inicialitza una llista buida per la pila.
        """
        self.pila = []

    def afegir(self, element):

        self.pila.append(element)

        """
        Afegeix un element a la part superior de la pila.

        Paràmetres:
        - element: qualsevol tipus d'element.
        """

    def extreure(self):

        if len(self.pila) > 0:
            extraccio = self.pila.pop()
            return extraccio
        else:
            print("Error, la pila està buida")
        """
        Extreu i retorna l'últim element afegit (part superior de la pila).
        Llença un error si la pila està buida.
        """

    def veure_darrer(self):
        if len(self.pila) > 0:
            darrer = self.pila[-1]
            return darrer
        else:
            print("Error, la pila està buida")
        """
        Retorna l'últim element afegit sense extreure'l.
        Llença un error si la pila està buida.
        """

    def buit(self):

        if len(self.pila) > 0:
            return True
        else:
            return False
        """
        Retorna True si la pila està buida, False en cas contrari.
        """

    def longitud(self):
        longpila = len(self.pila)
        return longpila
        """
        Retorna el nombre d'elements de la pila.
        """

pila = ColaLifo()
pila.afegir("A")
pila.afegir("B")
pila.afegir("C")

print(pila.veure_darrer())  # Sortida: "C" (últim element afegit)
print(pila.extreure())      # Sortida: "C"
print(pila.veure_darrer())  # Sortida: "B"
print(pila.longitud())      # Sortida: 2
print(pila.buit())          # Sortida: False
pila.extreure()
pila.extreure()
print(pila.buit())          # Sortida: True (ja que no hi ha res)