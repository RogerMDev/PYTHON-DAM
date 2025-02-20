import heapq

#cua de prioritat buida

class CuaDocuments:
    def __init__(self):

        self.cua_prioritat = []

    def AfegirDocument(self, prioritat, nom_document):

        heapq.heappush(self.cua_prioritat, (prioritat, nom_document))

        print(f"S'ha afegit el document {nom_document} amb prioritat {prioritat}")

    def ImprimirTreball(self):
        if self.cua_prioritat:
            prioritat, nom_document = heapq.heappop(self.cua_prioritat)
            print ( f"Imprimint el treball {self.nom_document} ...")
        else:
            print("No hi ha documents a la cua per imprimir")

P = CuaDocuments()
while True:

    print(f"1. Afegir document")
    print(f"2. Imprimir treball")
    print(f"3. Finzalitzar programa")
    opcio = int(input(f"Escull una de les opcions: "))

    if opcio == 1 :

        nom_document = input(f"Digues el nom del document")
        prioritat = input("Digues la prioritat del document")
        P.AfegirDocument(prioritat, nom_document)

    elif opcio ==2 :
        P.ImprimirTreball()

    elif opcio == 3:
        print(f"Sortint del programa")
        break

    else:
        print(f"Opció no vàlida. Torna-ho a intentar...")

















