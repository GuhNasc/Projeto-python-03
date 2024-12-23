###### IF ############
# Nada mais que uma checagem de variavel.

#x = int(input("Digite o valor de X: "))
#
#if x >= 5:
#    print("X é maior ou igual a 5")
#else:
#    print("X é menor que 5")

###### FOR ################

# serve para iterar algo, somar alguma variavel ate que chegue em algum valor especifico.

#for i in range(1,5): #Aqui meu I vai começar em 1 e vai rodar esse loop até o valor final (5)
#    print(i)

#lista_convidados = ['Gustavo', 'Joao', 'Felipe', 'Lucas']
#
#for convidado in lista_convidados:
#    print(convidado)


############# WHILE ###############
# Criando um codigo que roda infinito
import time

cond = True

while cond:
    print("O pai é bom")
    time.sleep(1)