def levenshtein_distance(primeira, segunda):
    linhas = len(primeira) + 1
    colunas = len(segunda) + 1
    tabela = [[0] * colunas for _ in range(linhas)]

    for linha in range(linhas):
        tabela[linha][0] = linha
    for coluna in range(colunas):
        tabela[0][coluna] = coluna

    for linha in range(1, linhas):
        for coluna in range(1, colunas):
            custo = 0 if primeira[linha - 1] == segunda[coluna - 1] else 1
            tabela[linha][coluna] = min(
                tabela[linha - 1][coluna] + 1,
                tabela[linha][coluna - 1] + 1,
                tabela[linha - 1][coluna - 1] + custo,
            )

    return tabela[-1][-1]


senha_antiga = "gatinho123"

while True:
    senha_nova = input("Digite a nova senha: ")
    distancia = levenshtein_distance(senha_antiga, senha_nova)

    if distancia < 4:
        print("Senha muito parecida com a antiga!")
    else:
        print("Senha alterada com sucesso!")
        break
