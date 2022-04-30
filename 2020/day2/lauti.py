with open ("input.txt") as lineas:

    linea = lineas.readlines()
    total = 0

for l in linea:
    if l[:-1]: 
        quitar = l.split(" ")
        probar = quitar[0]
        numBajos = int(probar.split("-")[0])
        numAltos = int(probar.split("-")[1])
        probar2 = quitar[1]
        letras = probar2[0]
        contra = probar[2]
        encontradas = 0
        print(contra)
        for cart in contra:
            if cart == letras:
                encontradas += 1
        if encontradas >= numBajos and encontradas <= numAltos:
            total += 1

print(total)
