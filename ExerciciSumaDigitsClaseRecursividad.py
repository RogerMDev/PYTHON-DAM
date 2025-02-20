
def sumadigitos(n):
    if n < 10:
        return n
    else:
        return sumadigitos(n%10) + sumadigitos(n // 10 )


resultado = sumadigitos(45)
print (resultado)

