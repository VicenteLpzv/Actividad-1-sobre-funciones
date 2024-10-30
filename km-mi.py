#escribir una funcion que convierta kilometros a millas y viceversa

def km_mi(a):
    conve = a * 0.621371
    return conve

def mi_km(a):
    conve = a*1.60934
    return conve

while True:
    try:
        n = input("1) Kilómetros a millas.  2) Millas a kilómetros: ")
        if n == "1":
            a = float(input("Ingresa la distancia en kilómetros: "))
            conversion = km_mi(a)
            print(f"La conversión a millas es: {conversion:.2f}")
            break  # Salir del ciclo tras una conversión exitosa 
        elif n == "2":
            a = float(input("Ingresa la distancia en millas: "))
            conversion = mi_km(a)
            print(f"La conversión a kilómetros es: {conversion:.2f}")
            break  # Salir del ciclo tras una conversión exitosa  
        else:
            print("Error: Por favor, ingresa '1' o '2' para seleccionar una opción válida.")

    except ValueError:
        print("Error: Entrada inválida. Por favor, ingresa un número válido.")

    
