#EXERCICI 1 SOBRE COMANDES EN UNA BOTIGA

#CREEM EL DICCIONARI

dicc_botiga= {
    "Anna": [("Llibre", 2, 10.0), ("Motxilla", 1, 30), ("Bolígraf",4, 2.50)],
    "Carles": [("Videojoc", 2, 30)],
    "Antoni": [("Ordinador", 1, 800.0), ("Ratolí", 1, 20.0), ("Teclat",3 , 30)],
    "Oscar": [("Eines", 3 , 30), ("Adhesius", 4, 10)],
}

while True :
    #Es mostra el menú d'opcions
    print("1. Mostrar el cost total de les comandes dels clients")
    print("2. Llistar tots els clients que han fet comandes totals per sobre de 100€")
    print("3. Imprimir les comandes realitzades per un usuari sol·licitat per scanner")
    print("4. Sortir del programa")

    opcio = int(input("Escull una opcio: "))
    if opcio == 1:
        if dicc_botiga:
            for client, comandes in dicc_botiga.items():
                cost_total_usuari = sum(quantitat * preu for _, quantitat, preu in comandes)
                print(f"El cost total de les comandes del client {client} és de {cost_total_usuari:.2f}€")
        else:
            print("No existeix cap diccionari a la base de dades ")

    elif opcio == 2:
        if dicc_botiga:
            print(f"Els següents usuaris han fet compres iguals o superiors a 100€:")
            for client, comandes in dicc_botiga.items():
                cost_total_usuari = sum(quantitat * preu for _, quantitat, preu in comandes)
                if cost_total_usuari >= 100:
                    print(f"{client}")
        else:
            print("No existeix cap client a la base de dades")

    elif opcio == 3:

        client_seleccionat = input("Digues el nom del usuàri/a del que vols veure les comandes:")

        print(f" Mostrant les comandes que ha fet el client {client_seleccionat}: {dicc_botiga[client_seleccionat]}")

    elif opcio == 4:
        print("Sortint del programa...")
        break

    else:
        print("Selecciona un nombre vàlid")



