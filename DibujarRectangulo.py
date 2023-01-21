def draw(wight,hight):
    for i in range(hight):
        for j in range(wight):
            print("* ",end="")
        print()
      

print('''\t.:MENU:.
Dibujemos un rectángulo
Digite Anchura y Altura''')
wight = int(input('Cual es la anchura del rectángulo? -> '))
hight = int(input('Cual es la altura del rectángulo? -> '))
print()
draw(wight,hight)