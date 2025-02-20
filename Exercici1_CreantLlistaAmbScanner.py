#EXERCICI 1 SOBRE COMANDES EN UNA BOTIGA

#CREEM EL DICCIONARI
dicc_botiga = {}
llista_engloba_tuples = []
tupla_botiga = ()
suma_preu = 0

while True :
    #Es mostra el menú d'opcions
    print("1. Afegir contacte i especificacions producte")
    print("2. Imprimir informació guardada")
    print("3. Mostrar el cost total de la comanda de cada client")
    print("4. Llistar tots els clients que han fet comandes totals per sobre de 100€")
    print("5. Sortir del programa")

    opcio = int(input("Escull una opcio: "))

    if opcio == 1:
        #Afegim un nou contacte
        nom_usuari = input("Digues el nom de l'usuari/a: ")
        nom_producte = input("Digues quin producte ha comprat: ")
        quantitat_producte = int(input("Digues quina quantitat ha comprat: "))
        preu_unitari = float(input("Digues el preu unitari del producte que ha comprat: "))

        tupla_botiga = (nom_producte, quantitat_producte, preu_unitari)

        dicc_botiga[nom_usuari] = llista_engloba_tuples.append(tupla_botiga)

        print("Informació guardada correctament")

    elif opcio == 2:
        if dicc_botiga:
            nom_usuari = input("Digues el nom del client que vols consultar")
            if nom_usuari in dicc_botiga:
                print("Informació actual:")
                for nom_usuari in dicc_botiga.items():
                    print(f"{nom_usuari}: ")
                for tupla_botiga in llista_engloba_tuples:
                    print(f" Producte: {tupla_botiga[0]}, Quantitat: {tupla_botiga[1]}, Preu unitari: {tupla_botiga[2]}")
            else:
                print("Aquest client no existeix a la base de dades")
        else:
            print("No hi ha cap client a la base de dades")

    elif opcio == 3:
        if dicc_botiga:
            nom_usuari = input("Digues el nom del client que vols calcular l'import total")
            if nom_usuari in dicc_botiga:
                for tupla_botiga in llista_engloba_tuples:
                    preu_suma = tupla_botiga[1]*tupla_botiga[2]

                    suma_preu =+ preu_suma

                print(f"La suma dels productes del client {nom_usuari} són : {suma_preu} €")

            else:
                print(f"No hi ha cap usuari amb el nom {nom_usuari} registrat")

        else:
            print("No hi ha cap client a la base de dades")

    elif opcio == 4:
        if dicc_botiga:
            for nom_usuari, tupla_botiga in dicc_botiga:

                    preu_suma = tupla_botiga[1]*tupla_botiga[2]

                    suma_preu =+ preu_suma

                if suma_preu >= 100:
                    print(f"Usuaris/es que presenten comandes per sobre de 100€: {nom_usuari} ")

        else:
            print("No hi ha cap client a la base de dades")


    elif opcio == 5:
        print("Sortint del programa...")
        break

    else:
        print("Selecciona un nombre vàlid")



