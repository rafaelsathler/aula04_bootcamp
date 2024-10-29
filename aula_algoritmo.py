lista: list = [40,50,60,70,0,-408593,1,50]


def ordernar_lista(numeros:list) -> list:
    nova_lista_de_num = numeros.copy()
    for i in range(len(nova_lista_de_num)):
        for j in range(i+1, len(nova_lista_de_num)):
            if nova_lista_de_num[i] > nova_lista_de_num[j]:
                nova_lista_de_num[i], nova_lista_de_num[j] = nova_lista_de_num[j], nova_lista_de_num[i]
    return nova_lista_de_num

nova_lista = ordernar_lista(lista)
print(nova_lista)