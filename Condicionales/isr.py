sueldo = float(input("Ingrese su sueldo: "))

if sueldo <= 578.52:
    inferior = 0.01
    porcentaje = 1.92
    cuota = 0
elif sueldo <= 4910.18:
    inferior = 578.53
    porcentaje = 6.4
    cuota = 11.11

isr = (sueldo - inferior) * porcentaje / 100 + cuota
sueldo_final = sueldo - isr
print(f"El ISR fue de: ${isr:,.2f}")
print(f"Tu sueldo final es de: ${sueldo_final:,.2f}")
    