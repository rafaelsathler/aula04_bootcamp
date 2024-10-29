# 16 - Escreva uma função que receba uma lista de números e retorne a soma de todos os números. 

#lista = [*range(1,11)]

#def soma_todos_os_num(lista: list) -> int:
#    somatoria = 0
#    for i in range(len(lista)):
#        somatoria += lista[i]
#    return somatoria

#total = soma_todos_os_num(lista)
#print(total) 

# 17 - Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.     

#num: int = int(input("Favor inserir um número inteiro: "))

#def analise_primo_ou_nprimo(numero: int) -> bool:
#    qnt = 0

#    if numero >= 1:
#        for i in range(1, numero):
#            if numero % i == 0:
#                qnt += 1

#        if qnt == 1:
#            analise = True
#        else:
#            analise = False       
                        
#   return analise

#resultado = analise_primo_ou_nprimo(num)
#print(resultado)

# 18 - Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

texto: str = str(input("Favor inserir um texto: "))

def revesao_do_texto(text: str) -> str:
    return text[::-1]

print(revesao_do_texto(texto))
