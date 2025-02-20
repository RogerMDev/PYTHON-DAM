import hashlib

# Definir la entrada (string a hashear)
texto = "Hola mundo"

# Convertir el texto a bytes, ya que hashlib trabaja con bytes
texto_bytes = texto.encode('utf-8')

# Crear el objeto hash usando, por ejemplo, el algoritmo SHA-256
hash_obj = hashlib.sha256(texto_bytes)

# Obtener la representación hexadecimal del hash
hash_hex = hash_obj.hexdigest()

print("Texto original:", texto)
print("Hash (SHA-256):", hash_hex)