#1


def obtener_existencias(matriz: list, depositos: list, tipos: list) -> list:

    if type(matriz) != list or type(depositos) != list or type(tipos) != list:
        mensaje = "Se esperaba una lista"
        return mensaje
    

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Ingrese un numero para {depositos[i]} y {tipos[j]} "))

    return matriz

#2
def calcular_cantidad_juguetes(matriz: list) -> list:
    if type(matriz) != list:
        mensaje = "Se esperaba una lista"
        return mensaje
    
    suma_total = [0] *len(matriz)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):   
            suma_total[i] += matriz[i][j] 

    return suma_total

#3
def necesario_reponer (matriz: list, depositos: list, tipos: list):
    if type(matriz) != list or type(depositos) != list or type(tipos) != list:
        mensaje = "Se esperaba una lista"
        return mensaje
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < 500:
                print(depositos[i], tipos[j])

#tipos = ["Autos", "muñecas", "trenes", "peluches", "spinners", "cartas"]

#4 Máxima cantidad de juguetes almacenados de cada tipo. Devolver en qué 
# provincia se encuentran.

#5
def calcular_mayor_recaudacion(matriz: list, precios: list, deposito: list, tipo: list):
    
    suma_total = calcular_cantidad_juguetes(matriz)
    bandera_mayor = False
    mayor_recaudado = 0
    precio_total = [0] *len(suma_total)

    deposito_mayor_recaudado = [0]
    for i in range(len(matriz)):
        precio_total[i] += precios[i] * suma_total[i]
        
    
    for i in range(len(deposito)):
        if bandera_mayor == False or mayor_recaudado < precio_total[i]:
            deposito_mayor_recaudado = deposito[i]
            mayor_recaudado = precio_total[i]
            bandera_mayor = True
    
    print(deposito_mayor_recaudado)
           

#6
def calcular_mayor_50k(matriz: list, depositos: list ):
    cantidad_total = calcular_cantidad_juguetes(matriz)

    for i in range(len(cantidad_total)):
        if cantidad_total[i] > 50000:
            print(f"{depositos[i]} cuenta con una cantidad de: {cantidad_total[i]} unidades totales")

#7
#tipos = ["autos", "muñecas", "trenes", "peluches", "spinners", "cartas"]
def calcular_almacenados(matriz: list, tipos: list) -> list:
    if type(matriz) != list or type(tipos) != list:
        mensaje = "Se esperaba una lista"
        return mensaje
    
    suma_tipo = [0, 0, 0, 0, 0, 0] 
    suma_total = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if tipos[j] == "autos":
                suma_tipo[j] += matriz[i][j] 
            elif tipos[j] == "muñecas":
                suma_tipo[j] += matriz[i][j]
            elif tipos[j] == "trenes":
                suma_tipo[j] += matriz[i][j]
            elif tipos[j] == "peluches":
                suma_tipo[j] += matriz[i][j]
            elif tipos[j] == "spinners":
                suma_tipo[j] += matriz[i][j]
            else:
                suma_tipo[j] += matriz[i][j]

            

    return suma_tipo

def calcular_porcentaje(matriz: list, tipos: list):
    matriz_total = calcular_almacenados(matriz, tipos)
    suma_total = 0
    porcentaje = 0

    for i in range(len(matriz_total)):
        suma_total += matriz_total[i]
    
    for i in range(len(matriz_total)):
        porcentaje = matriz_total[i] / suma_total * 100
        print(porcentaje)
    
    
    




#9 
def carga_aleatoria(matriz: list) -> list:

    seguir = "si"

    while seguir == "si":
        fila = int(input("Ingrese la fila: "))
        columna = int(input("Ingrese la columna: "))
        numero = int(input("Ingrese el valor a ingresar: "))
        matriz[fila][columna] = numero
        seguir = int(input("Desea continuar ingresando? si/no")).lower()

    return matriz


    