# Exercícios de Distância de Levenshtein

Este repositório contém seis exercícios em Python para praticar a **distância de Levenshtein**, uma medida do número mínimo de inserções, remoções ou substituições necessárias para transformar uma palavra em outra.

## Objetivos

Os exercícios praticam:

- Implementação da função `levenshtein_distance`;
- Comparação entre palavras;
- Uso de `input()`, condicionais e mensagens ao usuário;
- Busca pelo item mais próximo em uma lista;
- Aplicação de limite de tolerância;
- Uso de laços `for` e `while`;
- Criação de um corretor simples de palavras.

## Estrutura do projeto

Os scripts estão na pasta [`exercicios/`](./exercicios/):

| Arquivo | Descrição |
|---|---|
| [`exercicio1.py`](./exercicios/exercicio1.py) | Compara quatro pares de palavras e mostra suas distâncias. |
| [`exercicio2.py`](./exercicios/exercicio2.py) | Classifica duas palavras como idênticas, parecidas ou diferentes. |
| [`exercicio3.py`](./exercicios/exercicio3.py) | Sugere o item de jogo mais próximo do texto digitado. |
| [`exercicio4.py`](./exercicios/exercicio4.py) | Aceita ou recusa sugestões usando um limite de tolerância igual a `2`. |
| [`exercicio5.py`](./exercicios/exercicio5.py) | Impede a criação de uma senha muito parecida com a senha antiga. |
| [`exercicio6.py`](./exercicios/exercicio6.py) | Sugere o nome de país mais próximo da entrada do usuário. |

Cada arquivo é independente e contém sua própria implementação da função `levenshtein_distance`.

## Como executar

É necessário ter Python instalado. Na raiz do projeto, execute qualquer exercício com:

```powershell
python exercicios\exercicio1.py
```

Para executar outro exercício, substitua o nome do arquivo:

```powershell
python exercicios\exercicio6.py
```

Os exercícios que usam `input()` solicitarão dados diretamente no terminal.

## Exemplo

Ao executar o Exercício 1, uma das saídas será:

```text
casa -> caso: distância 1
```

No Exercício 6, uma entrada como `Brazl` pode gerar:

```text
O país mais próximo é: Brasil (distância 2)
```

## Fórmula usada

Para cada par de palavras, o algoritmo constrói uma tabela de custos. Cada posição considera o menor custo entre:

1. Remover um caractere;
2. Inserir um caractere;
3. Substituir um caractere, quando necessário.

Assim, a distância `0` indica palavras idênticas, enquanto valores maiores indicam mais diferenças entre elas.
