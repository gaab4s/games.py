def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y

while True:
    print("Opções:")
    print("Digite '1' para realizar uma soma")
    print("Digite '2' para realizar uma subtração")
    print("Digite '3' para realizar uma multiplicação")
    print("Digite '4' para realizar uma divisão")
    print("Digite '0' para sair")

    escolha = input("Digite a opção desejada: ")

    if escolha == '0':
        print("Encerrando a calculadora.")
        break

    if escolha not in ('1', '2', '3', '4'):
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado: ", soma(num1, num2))
    elif escolha == '2':
        print("Resultado: ", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado: ", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado: ", divisao(num1, num2))
