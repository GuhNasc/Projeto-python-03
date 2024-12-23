# 1 Contar palavras dentro de um texto

#frase = "Meu nome e Gustavo e sou engenheiro de dados"
#
#palavras = frase.split(" ")
#
#print(palavras)
#
#contador = {}
#
#            # percorrer todas as palavras dentro da lista e verificar se estao dentro da lista
#for palavras in palavras:
#    if palavras in contador:
#        contador[palavras] = +1
#    else:
#        contador[palavras] = 1


# 2 Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

#quantidade = int(input("Digite o valor: ")) 
#preco = float(input("Digite o preço: "))
#
#if quantidade > 0 and preco > 0:
#    print("Dados validos")
#else:
#    print("Dados invalidos")

# 3 Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

#temperatura = float(input("Digite a temperatura para verificação: "))
#
#if temperatura < 18:
#    print("Temperatura baixa")
#elif temperatura >= 18 and temperatura <= 26:
#    print("Temperatura normal")
#else:
#    print("Temperatura Alta")


# 4 Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um registro de log em formato de dicionário como 
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

#log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
#
#if log['level'] == 'ERROR':
#    print(log['message'])


# 5 Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

#idade = int(input("Digite sua idade: "))
#
#if idade < 18 or idade > 65:
#    print("Você nao tem idade necessaria")
#else:
#    print("Idade valida")
#
#
#email = str(input("Digite seu e-mail: "))
#if '@' not in email:
#    print("Email invalido")
#else:
#    print("E-mail valido")

# 6 Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

#transacao = {'valor': 12, 'hora': 20}
#
#if transacao['valor'] > 10000 or transacao['hora'] > 18 or transacao['hora'] < 9:
#    print("Transação invalida")
#else:
#    print("Trasaçãoc valida")

########################################### FOR ##############################

# Contar letras de uma palavra
#words = ['cat', 'window', 'defenestrate']
#for w in words:
#    print(w, len(w))


# Conta de 0 até 4
#for i in range(5):
#    print(i)

#list(range(5, 10)) aqui começa em 5 e vai ate o 9 (10 nao é incluso)
#[5, 6, 7, 8, 9]
#
#list(range(0, 10, 3)) aqui começa no 0 e vai ate o 10, PORÉM eu tenho um STEP de 3, OU SEJA, vai de 3 em 3
#[0, 3, 6, 9]
#
#list(range(-10, -100, -30)) mesma coisa que no de cima poré com numeros negativos
#[-10, -40, -70]

# usando len e range no mesmo codigo
#a = ['Mary', 'had', 'a', 'little', 'lamb']
#for i in range(len(a)):
#    print(i, a[i])

# 7 Normalizando os numeros
#numeros = [10, 20, 30, 40, 50]
#minimo = min(numeros)
#maximo = max(numeros)
#normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]
#
#print(normalizados)

# 8 verficação de dados faltantes

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

print(usuarios_validos)

# 9 SOMENTE PARES

numeros = range(1, 11)
pares = [x for x in numeros if x % 2 == 0]

print(pares)

# 10 total de vendas por categoria

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)



########################################## WHILE ############################################


# 11 verificando numeros entre range de 1 e 10
numero = int(input("Digite um número entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("Número fora do intervalo!")
    numero = int(input("Por favor, digite um número entre 1 e 10: "))

print("Número válido!")



# 12 Consumo de API Simulado
pagina_atual = 1
paginas_totais = 5  # Simulação, na prática, isso viria da API

while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais}")
    # Aqui iria o código para processar os dados da página
    pagina_atual += 1

print("Todas as páginas foram processadas.")