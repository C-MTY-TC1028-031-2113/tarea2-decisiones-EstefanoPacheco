
def main():
    edad = int(input("Ingresa tu edad: "))

    if edad >= 18: 
        identificacion = input("¿Tiene identificación oficial? (s/n): ")
        if identificacion == "s":
            print("Trámite de licencia concedido")
        elif identificacion == "n":
            print("No cumples requisitos")
        else: "Respuesta incorrecta"
    else: print("No cumples requisitos")


if __name__ == '__main__':
    main()
