import random 


def calc_pi(n):
    nombre_cercle = 0
    nombre_total = 0
    
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            nombre_cercle += 1
        nombre_total += 1

    return 4* nombre_cercle / nombre_total

t = int(input ('le nombre N: '))
h = calc_pi(t)
print(h)