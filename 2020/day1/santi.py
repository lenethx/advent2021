with open ("input.txt" , "r" ) as lean: 

    lineas=lean.readlines()


for linea in lineas:
    #print(linea[:-1])
    for linea2 in lineas:
        if int(linea2[:-1]) + int(linea[:-1]) == 2020:
            print(linea, linea2)
            print(int(linea2[:-1]) * int(linea[:-1]))