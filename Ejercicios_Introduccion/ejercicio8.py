# Calcula la multiplicación y la suma de dos números. 
# Dados dos números enteros, devuelve su producto sólo si el producto es mayor que 1000, de lo contrario, devuelve su suma.

# FUNCIONES (OJO!!!! Las funciones siempre van primeras)
def suma(num1, num2):
    
    return num1 + num2

def multiplicacion(num1, num2):

    return num1 * num2

# OPERACIONES
num1 = float(input("Introduzca un número: "))
num2 = float(input("Introduzca otro número: "))

producto = multiplicacion(num1, num2)

if producto > 1000 :
    print(f"El producto de {num1} y {num2} es {producto}")

elif 0 < producto: 
    print(f"La suma de {num1} y {num2} es {suma(num1, num2)}")