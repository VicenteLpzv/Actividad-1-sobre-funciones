#Vicente Y. Lopez V.  240010
#funcion que convierta minutos a horas y minutos

def min_hrsmn (t):
    con = t /60
    conm = t % 60
    return con, conm

while True:
    try:
        t = int(input("Ingresa los minutos: "))
        r = min_hrsmn(t)
        print (f"{t} minutos equivalen a {r[0]:.0f} horas y {r[1]:.0f} minutos")
        break
    except ValueError: print ("Invalido")
        