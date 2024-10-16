from Ejercicios import ejercicios

depositos = ["PBA", "CABA", "Chubut", "Tucuman", "Mendoza"]
tipos = ["autos", "muñecas", "trenes", "peluches", "spinners", "cartas"]
cantidad = []
precios = [500, 200, 1000, 150, 400, 50]

matriz = [[523, 100, 6, 298, 499, 500],
           [1, 2, 3, 4, 5, 4],
           [10, 20, 78, 40, 501, 600],
           [13, 152, 123, 161, 858, 151],
           [500, 183, 1357, 475, 1374, 475]]

# matriz = [[0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0]]

#1
# matriz_a = ejercicios.obtener_existencias(matriz, depositos, tipos)
# print(matriz_a) 

#2
# matriz_a = ejercicios.calcular_cantidad_juguetes(matriz)
# for i in range(len(depositos)):           
#     print(f"en {depositos[i]} hay un total de: {matriz_a[i]}")

#3
# ejercicios.necesario_reponer(matriz, depositos, tipos)

#5
ejercicios.calcular_mayor_recaudacion(matriz, precios, depositos, tipos)


#6
# ejercicios.calcular_mayor_50k(matriz, depositos)
