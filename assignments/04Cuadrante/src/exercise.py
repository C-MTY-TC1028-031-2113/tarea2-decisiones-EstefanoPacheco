def main():
    # Escribe tu código abajo de esta línea
    grados = int(input("Introduce los grados: "))

    if 0 <= grados <= 360:
        if grados == 0 or grados == 90 or grados == 180 or grados == 270 or grados == 360:
            print("eje")
        elif 0 < grados < 90:
            print("cuadrante 1")
        elif 90 < grados < 180:
            print("cuadrante 2")
        elif 180 < grados < 270:
            print("cuadrante 3")
        else: print("cuadrante 4")
    else: print("excede")

if __name__ == '__main__':
    main()
