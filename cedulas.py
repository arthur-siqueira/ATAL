# Lê o valor inteiro da entrada
valor_lido = int(input())

# Guarda o valor original para imprimi-lo no início
valor_decomposicao = valor_lido

# Imprime o valor lido, conforme a saída esperada
print(valor_decomposicao)

# Lista das notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Itera sobre cada valor de nota para calcular a quantidade
for nota in notas:
    # Calcula a quantidade de notas usando a divisão inteira
    quantidade = valor_decomposicao // nota

    # Imprime a quantidade no formato especificado
    print(f"{quantidade} nota(s) de R$ {nota},00")

    # Atualiza o valor restante usando o operador módulo (resto da divisão)
    valor_decomposicao = valor_decomposicao % nota