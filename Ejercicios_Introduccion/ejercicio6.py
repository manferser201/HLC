# Acepte una lista de 5 números flotantes como entrada del usuario.

lista = []
i = 0

while i < 5 :
    num = input("Introduzca un numero: ")
    lista.insert(i, num)

    i += 1

print(lista)