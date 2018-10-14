#Autor: Saúl Figueroa Conde.
#Matrícula: A01747306.
#Grupo 02.
#Este programa muestra el uso de los ciclos while. Primero despliega un menu en el que el usuario puede escoger entre
#tres opciones. La primera ejecuta una función que imprime el cociente y residuo de una división. La segunda opcion
#ejecuta uan función que encuentra e imprime el mayor de un conjunto de valores enteros positivos que teclea el usuario.
#El menu se sigue desplegando hasta que el usuario decida escoger la tercera opción 'Salir' que termina el programa.
#----------------------------------------------------------------------------------------------------------------------


#Se declara la función encontrarMayor. No recibe parámetros. Encuentra e imprime el mayor de un conjunto de valores
#enteros positivos que teclea el usuario. Se hace uso de un solo ciclo while. El usuario indica que ha terminado de
#teclear valores cuando escribe '-1'. No se hace uso de listas, diccionarios ni conjuntos.
def encontrarMayor():
    numeroAnterior = -1
    numeroActual = 0
    contadorNumero = 0

    print("Teclea una serie de números para encontrar el mayor.")

    while numeroActual != -1:
        numeroActual = int(float(input(("Teclea un número [-1 para salir]:"))))

        if numeroActual > numeroAnterior:
            numeroAnterior = numeroActual
            contadorNumero += 1

        elif numeroActual < -1:
            print("Ese no es un valor válido: Debes teclear un número entero positivo.")

        elif numeroActual == -1:
            if contadorNumero != 0:
                print("El mayor es: {}".format(numeroAnterior))
            else:
                print("No hay valor mayor")

    pausa = input("Presione enter para continuar...")
    print("")


#Se declara la función dividir. Esta función recibe como parámetros el dividendo y el divisor dados por el usuario y
#calcula e imprime el valor del conciente y el residuo haciendo uso de un solo ciclo while. No se usa ninguno de los
#siguientes operadores: '/', '//' ni '%'.
def dividir(dividendo, divisor):
    cociente = 0
    residuo = 0
    dividendoBackup = dividendo

    while dividendo >= divisor:
        dividendo -= divisor
        cociente = cociente + 1

    residuo = dividendo

    if residuo == divisor:
        residuo = 0

    print("{} / {} = {}, sobra {}".format(dividendoBackup, divisor, cociente, residuo))
    pausa = input("Presione enter para continuar...")
    print("")


#Se declara la función main. Se despliega un menu en el que el usuario puede elegir entre tres opciones. La primera
#llama a la función dividir y la segunda a encontrarMayor. El menú se sigue desplegando/imprimiendo mientras el usuario
#no escoja la opcion tres. Si se selecciona una opcion incorrecta se despliega un mensaje de error.
def main():
    opcion = 0

    while opcion != 3:

        if opcion < 0 or opcion > 3:
            print("ERROR, teclea 1, 2 o 3")
            pausa = input("Presione enter para continuar...")
            print("")
            opcion = 0

        elif opcion == 0:
            print("Misión 07. Ciclos while")
            print("Autor: Saúl Figueroa Conde")
            print("Matrícula: A01747306")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")

            opcion = int(input("Teclea tu opción: "))
            print("")

        elif opcion == 1:
            print("Calculando divisiones")
            dividendo = abs(int(float(input("Dividendo: "))))
            divisor = abs(int(float(input("Divisor: "))))

            dividir(dividendo, divisor)
            opcion = 0

        elif opcion == 2:
            encontrarMayor()
            opcion = 0

    mensajeSalida = input("Gracias por usar este programa, regrese pronto. [Enter para salir]...")


#Se llama a la función main para correr el programa.
main()