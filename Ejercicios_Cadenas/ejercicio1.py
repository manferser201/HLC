cadena = input("INTRODUZCA UNA CADENA MAYOR QUE 7 Y CUYA LONGITUD SEA IMPAR: ")

while len(cadena) < 7 or len(cadena)%2 == 0:
    print("LA CADENA TIENE QUE TENER COMO MÍNIMO UNA LONGITUD DE 7, ADEMÁS DE QUE DEBE SER UNA LONGITUD IMPAR")
    cadena = input("INTRODUZCA UNA NUEVA CADENA CON LOS PARÁMETROS CORRECTOS: ")

caracterDelMedio = cadena[round(len(cadena) / 2) - 1]
caracterAnteriorAlMedio = cadena[round(len(cadena) / 2) - 2]
caracterSiguienteAlMedio = cadena[round(len(cadena) / 2)]

print(f"El resultado es: {caracterAnteriorAlMedio}{caracterDelMedio}{caracterSiguienteAlMedio}")