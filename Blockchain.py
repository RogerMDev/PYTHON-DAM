import hashlib

# Información del "bloque": puede ser una cadena que represente datos del bloque
datos_bloque = "Transacciones del bloque anterior, marca de tiempo, root de merkle..."

# Queremos encontrar un nonce tal que el hash comience con '0000'
objetivo = "000000"

nonce = 0
while True:
    # Concatenamos los datos del bloque con el nonce
    datos_a_hashear = datos_bloque + str(nonce)

    # Calculamos el hash usando SHA-256
    hash_obj = hashlib.sha256(datos_a_hashear.encode('utf-8'))
    hash_hex = hash_obj.hexdigest()

    # Revisamos si el hash cumple con el objetivo (comenzar con '0000')
    if hash_hex.startswith(objetivo):
        print("¡Bloque minado con éxito!")
        print("Nonce encontrado:", nonce)
        print("Hash resultante:", hash_hex)
        break

    # Si no cumple, incrementamos el nonce y probamos de nuevo
    nonce += 1
