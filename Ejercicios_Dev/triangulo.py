def trifuerza(n:int):
    max = 2
    for triangulos in range(0, max):
        
        for fila in range(1,n+1):

            cantidad_asteriscos = 2 * fila - 1
            total = (2 * n - 1) * (max - triangulos) + 1
            relleno = int((total - cantidad_asteriscos) / 2)

            for _ in range(triangulos+1):
                for _ in range(relleno):
                    print(" ", end="")

                for _ in range(cantidad_asteriscos):
                    print("*", end="")

                for _ in range(relleno):
                    print(" ", end="")

                print(" ", end="")

            print()
    
    print()



n = int(input("Ingrese el número de filas de los triángulos: "))

trifuerza(n)
