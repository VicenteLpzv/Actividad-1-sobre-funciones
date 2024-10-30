#Vicente Y. Lopez V.  240010
#funcion que calcule el area de un circulo dependiendo su radio

def radio(r):
    area = 3.1416 * r**2
    return area

while True:
    try:
        r= float(input("Ingresa el radio del circulo: "))
        r=radio(r)
        print (f"el area del circulo es: {r:.2f}")
    except ValueError: print ("error")