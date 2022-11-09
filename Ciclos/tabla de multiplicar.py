
# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# ...
# 10 x 5 = 50

n = int(input("Ingresa el valor de n: "))

for i in range(1,11):
    mult = n * i
    print(f"{i} x {n} = {mult}")