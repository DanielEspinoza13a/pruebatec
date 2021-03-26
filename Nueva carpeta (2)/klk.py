datos = [4, [5, 6], [[9,5.9,[9,5,[5,8,6,9,3,6]],4,6,4], [7], 8, 9, 8, 512, [45, 6, 9, 865], 4, 5, [[[[6],8],6],5],10]]
lista = []

def lista_plana(datos):
    
    for x in datos:
        
        if type(x) == list:
            lista_plana(x)
        else:
            lista.append(x)

lista_plana(datos)

print(lista)