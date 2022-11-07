
calificacion = float(input("Ingresa tu calificación: "))

if calificacion >= 90:
    print("A")
else:
    if calificacion >= 80:
        print("B")
    else:
        if calificacion >= 70:
            print("C")
        else:
            if calificacion >= 60:
                print("D")
            else:
                print("F")

if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
elif calificacion >= 60:
    print("D")
else:
    print("F")