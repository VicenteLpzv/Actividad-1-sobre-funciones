#Vicente Y. Lopez V.  240010
#funcion que calcule factorial del numero dado

def factorial (a):
    fac = 1
    for i in range (1, a + 1):
     fac *= i
     print(f"Multiplicando {fac // i} * {i} = {fac}")
    return fac
while True:
    try:
        a =  int(input("Ingresa un numero para calcular su factorial: "))
        r= factorial (a)
        break
    except ValueError: print("Incorrecto")
print ("El factorial de ", a, " es: ", r)
