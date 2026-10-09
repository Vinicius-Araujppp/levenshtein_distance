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


paises = ["Brasil", "Argentina", "Chile", "Uruguai", "Paraguai", "Peru"]
digitado = input("Digite o nome de um país: ")
entrada_normalizada = digitado.strip().lower()

pais_mais_proximo = paises[0]
menor_distancia = levenshtein_distance(
    entrada_normalizada, pais_mais_proximo.lower()
)

for pais in paises[1:]:
    distancia = levenshtein_distance(entrada_normalizada, pais.lower())
    if distancia < menor_distancia:
        pais_mais_proximo = pais
        menor_distancia = distancia

print(f"Você digitou: {digitado}")
print(
    f"O país mais próximo é: {pais_mais_proximo} "
    f"(distância {menor_distancia})"
)
