import random


def inicializar_tablero():
    return [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]


def mostrar_tablero(tablero):
    print("+-------+-------+-------+")
    for fila in tablero:
        print("|       |       |       |")
        print("|   " + "   |   ".join(fila) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def verificar_ganador(tablero, jugador):

    for fila in tablero:
        if all(espacio == jugador for espacio in fila):
            return True
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False


def verificar_empate(tablero):
    return all(all(espacio in ['X', 'O'] for espacio in fila) for fila in tablero)


def obtener_movimiento_jugador(tablero):
    while True:
        try:
            movimiento = int(input("Ingresa tu movimiento (1-9): "))
            if movimiento < 1 or movimiento > 9:
                print("Movimiento inválido. Intenta de nuevo.")
                continue
            fila, columna = divmod(movimiento - 1, 3)
            if tablero[fila][columna] in ['X', 'O']:
                print("El cuadro ya está ocupado. Intenta de nuevo.")
            else:
                return fila, columna
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número del 1 al 9.")


def movimiento_maquina(tablero):
    movimientos_validos = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] not in ['X', 'O']]
    return random.choice(movimientos_validos)


def jugar_tic_tac_toe():
    tablero = inicializar_tablero()

    tablero[1][1] = 'X'
    mostrar_tablero(tablero)

    while True:

        fila, columna = obtener_movimiento_jugador(tablero)
        tablero[fila][columna] = 'O'
        mostrar_tablero(tablero)

        if verificar_ganador(tablero, 'O'):
            print("¡Felicidades! ¡Has ganado!")
            break
        if verificar_empate(tablero):
            print("El juego termina en empate.")
            break


        fila, columna = movimiento_maquina(tablero)
        tablero[fila][columna] = 'X'
        print(f"La máquina elige el cuadro {fila * 3 + columna + 1}")
        mostrar_tablero(tablero)

        if verificar_ganador(tablero, 'X'):
            print("La máquina ha ganado. Mejor suerte la próxima vez.")
            break
        if verificar_empate(tablero):
            print("El juego termina en empate.")
            break


jugar_tic_tac_toe()