import random

nums = []
for i in range (0,5):
    x = int(input("Inserte un número del 1 al 25: "))
    condicion1 = x < 1 or x > 25
    condicion2 = x in nums
    while (condicion1 == True or condicion2 == True):
        x = int(input("Número repetido o inválido, ingresar otro: "))
        condicion1 = x < 1 or x > 25
        condicion2 = x in nums
    nums.append(x)
    
print ("Estos son los números que ha elegido: " + str(nums)) 

numsA = []
for i in range (0,5):
    y = random.randint(1, 25)
    while (y in numsA):
        y = random.randint(1, 25)
    numsA.append(y)
print ("Estos son los números ganadores: " + str(numsA))

wins = 0
for x in nums:
    for y in numsA:
        if (x==y):
            wins+=1
if (wins == 0):
    print("Ningún número coincidió :( ¡Suerte para la próxima!")
elif (wins == 1):
    print("¡Felicidades! le diste a 1 número ganador")
elif (wins > 1):
    print("¡Suertudo! Has ganado con " +str(wins)+ " aciertos")
