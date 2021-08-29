import math

def main():
    # Escribe tu código abajo de esta línea
    a=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    
    if a == 0 and b == 0:
        print("No tiene solucion")
    elif a == 0 and b != 0:
        print(-c / b)
    else:
        d = (b**2) - (4*a*c)
        if d < 0:
            print("Raices complejas")
        elif d == 0:
            print(-b / (2*a))
        else: 
            print((-b + math.sqrt((b**2) - (4*a*c))) / (2*a))
            print((-b - math.sqrt((b**2) - (4*a*c))) / (2*a))

    # x1 = (-b + math.sqrt((b**2) - (4*a*c))) / (2*a)
    # x2 = (-b - math.sqrt((b**2) - (4*a*c))) / (2*a)
    # d = (b**2) - (4*a*c)
    
    


if __name__ == '__main__':
    main()
