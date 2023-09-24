import random

def criar_tabuleiro(linhas, colunas, bombas):
    tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]
    bombas_plantadas = 0

    while bombas_plantadas < bombas:
        x, y = random.randint(0, linhas - 1), random.randint(0, colunas - 1)
        if tabuleiro[x][y] != 'B':
            tabuleiro[x][y] = 'B'
            bombas_plantadas += 1

    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    for row in tabuleiro:
        print(" ".join(row))

def contar_bombas_vizinhas(tabuleiro, x, y):
    linhas, colunas = len(tabuleiro), len(tabuleiro[0])
    direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    count = 0

    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy
        if 0 <= nx < linhas and 0 <= ny < colunas and tabuleiro[nx][ny] == 'B':
            count += 1

    return count

def jogar():
    linhas = int(input("Digite o número de linhas do tabuleiro: "))
    colunas = int(input("Digite o número de colunas do tabuleiro: "))
    bombas = int(input("Digite o número de bombas: "))

    tabuleiro = criar_tabuleiro(linhas, colunas, bombas)
    tabuleiro_exibicao = [[' ' for _ in range(colunas)] for _ in range(linhas)]
    jogadas_restantes = linhas * colunas - bombas

    while jogadas_restantes > 0:
        print("\nTabuleiro atual:")
        imprimir_tabuleiro(tabuleiro_exibicao)
        x = int(input("\nDigite a linha: "))
        y = int(input("Digite a coluna: "))

        if x < 0 or x >= linhas or y < 0 or y >= colunas or tabuleiro_exibicao[x][y] != ' ':
            print("Jogada inválida. Tente novamente.")
            continue

        if tabuleiro[x][y] == 'B':
            print("\nVocê perdeu! Bomba encontrada.")
            imprimir_tabuleiro(tabuleiro)
            break

        bombas_vizinhas = contar_bombas_vizinhas(tabuleiro, x, y)
        tabuleiro_exibicao[x][y] = str(bombas_vizinhas)
        jogadas_restantes -= 1

    if jogadas_restantes == 0:
        print("\nVocê venceu! Parabéns!")
        imprimir_tabuleiro(tabuleiro_exibicao)

if __name__ == "__main__":
    jogar()
