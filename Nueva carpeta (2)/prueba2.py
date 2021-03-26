lista = [{'Nombre':'NUCLEO', 'Id':20, 'Tipo':'MP', 'Fuente':2},{'Nombre':'PVC de mexichem', 'Id':19, 'Tipo':'MP', 'Fuente':2}]

for elem in lista:
    for k,v in elem.items():
        print(k,v)