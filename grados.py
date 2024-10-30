#Vicente Y. Lopez V.  240010
#funcion que coniverta grados C a F y viceversa

def gc(c):
    f=(c*9/5) +32
    return f

def gf(f):
    c=(f-32)*5/9
    return c

while True:
    try:
        g = float(input("1) Celsius a Fahrenheit.   2) Fahrenheit a Celsius... "))
        if g == 1:
            c = float(input("Ingresa los grados Celsius: "))
            conversion = gc(c)
            print(f"La conversión a Fahrenheit es: {conversion:.2f}")
            break  # Salir del ciclo tras una conversión exitosa
        elif g == 2:
            f = float(input("Ingresa los grados Fahrenheit: "))
            conversion = gf(f)
            print(f"La conversión a Celsius es: {conversion:.2f}")
            break  # Salir del ciclo tras una conversión exitosa
        else:
            print("Opción invalida")
    except ValueError: print("Invalido")
        