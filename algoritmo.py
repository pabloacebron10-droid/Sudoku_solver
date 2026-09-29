def leer_tablero(nombre_fichero):
    tablero = []

    with open(nombre_fichero, "r") as fichero:

        for linea in fichero:

            fila = []

            for numero in linea.strip().split("|"):

                if numero != "":
                    fila.append(int(numero))

            tablero.append(fila)

    numero_maximo = 0

    for fila in tablero:

        for numero in fila:

            if numero > numero_maximo:
                numero_maximo = numero

    tamano_cuadrado = int(numero_maximo ** 0.5)

    return tablero, numero_maximo, tamano_cuadrado


def obtener_columna_actual(tablero, coordenadas):
    columna = coordenadas[1]

    columna_actual = []

    for fila in tablero:
        columna_actual.append(fila[columna])

    return columna_actual


def obtener_cuadrado_actual(tablero, coordenadas, tamano_cuadrado):
    fila = coordenadas[0]
    columna = coordenadas[1]

    inicio_fila = (fila // tamano_cuadrado) * tamano_cuadrado
    inicio_columna = (columna // tamano_cuadrado) * tamano_cuadrado

    cuadrado_actual = []

    for fila_actual in tablero[
        inicio_fila:inicio_fila + tamano_cuadrado
    ]:

        for numero in fila_actual[
            inicio_columna:inicio_columna + tamano_cuadrado
        ]:

            cuadrado_actual.append(numero)

    return cuadrado_actual


def resolver_tablero(tablero, numero_maximo, tamano_cuadrado):
    mascara = set(range(1, numero_maximo + 1))

    coordenadas = []

    fila = 0

    for valores in tablero:

        columna = 0

        for valor in valores:

            if valor == 0:
                coordenadas.append((fila, columna))

            columna += 1

        fila += 1

    for coordenada in coordenadas:

        fila_actual = tablero[coordenada[0]]

        candidatos = mascara - set(fila_actual)

        if len(candidatos) > 1:

            columna_actual = obtener_columna_actual(
                tablero,
                coordenada
            )

            candidatos -= set(columna_actual)

        if len(candidatos) > 1:

            cuadrado_actual = obtener_cuadrado_actual(
                tablero,
                coordenada,
                tamano_cuadrado
            )

            candidatos -= set(cuadrado_actual)

        if len(candidatos) == 1:

            tablero[coordenada[0]][coordenada[1]] = candidatos.pop()

    return tablero


tablero, numero_maximo, tamano_cuadrado = leer_tablero("sudoku.txt")

tablero = resolver_tablero(
    tablero,
    numero_maximo,
    tamano_cuadrado
)

print(tablero)