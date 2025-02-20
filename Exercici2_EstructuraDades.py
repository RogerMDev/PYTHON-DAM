
dicc_biblioteca = {
    1: {"titol": "Python per a tothom", "autor": "John Doe", "quantitat": 3},
    2: {"titol": "Dades i Estructures", "autor": "Anna Smith", "quantitat": 5},
    3: {"titol": "Introducció a OOP", "autor": "Joan Costa", "quantitat": 2},
    4: {"titol": "Git y GitHub" , "autor": "Midudev", "quantitat": 0},
}

#MOSTREM OPCIONS DEL MENÚ

while True:
    print(f"Benvingut, escull una opció: ")
    print(f"1. Afegir un nou llibre")
    print(f"2. Buscar un llibre")
    print(f"3. Mostrar nomès els llibres disponibles")
    print(f"4. Mostrar tots els llibres")
    print(f"5. Préstec d'un llibre")
    print(f"6. Sortir del programa")

    opcio = int(input("Digues quina opció vols executar "))

    if opcio == 1:
        ID_llibre = int(input("Digues l'ID del llibre"))
        titol = input("Digues el titol del llibre")
        autor = input("Digues l'autor/a del llibre")
        quantitat = int(input("Digues la quantitat a afegida"))

        dicc_biblioteca[ID_llibre] = {"titol": titol, "autor": autor, "quantitat": quantitat}
        print("Informació guardada correctament")

    elif opcio == 2:
        ID_llibre = int(input("Digues quin ID té el llibre que busques"))

        if ID_llibre in dicc_biblioteca:
            print(f"La informació del llibre amb l'ID  {ID_llibre} és la següent: {dicc_biblioteca[ID_llibre]}")

        else:
            print("No hi ha cap llibre registrat amb aquest ID")

    elif opcio == 3:
        print("Mostrant nomès els llibres disponibles: ")
        for ID_llibre in dicc_biblioteca:
            if dicc_biblioteca[ID_llibre]["quantitat"] > 0:
                llibre = dicc_biblioteca[ID_llibre]
                print(f"ID: {ID_llibre}, Títol: {llibre['titol']}, Autor: {llibre['autor']}, Quantitat: {llibre['quantitat']}")
            print()

    elif opcio == 4:
        print("Mostrant tots els llibres")
        for ID_llibre in dicc_biblioteca:
            llibre = dicc_biblioteca[ID_llibre]
            print(f"ID: {ID_llibre}, Títol: {llibre['titol']}, Autor: {llibre['autor']}, Quantitat: {llibre['quantitat']}")
        print()

    elif opcio == 5:
        ID_llibre = int(input("Digues quin ID té el llibre a prestar"))

        if ID_llibre in dicc_biblioteca:
            if dicc_biblioteca[ID_llibre]["quantitat"] > 0:
                dicc_biblioteca[ID_llibre]["quantitat"] -= 1
                print(f"LLibre amb l'ID {ID_llibre} prestat correctament")
            else:
                print(f"No hi ha llibres amb l'ID {ID_llibre} per prestar")
        else:
            print("Llibre no trobat")

    elif opcio == 6:
        print("Sortint del programa...")
        break

    else:
        print("Selecciona una opció vàlida")













