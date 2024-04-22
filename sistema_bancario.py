# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato

# Será permitido realizar 3 saques diários com limite máximo de R$ 500. Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato.

# Extrato: deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. "R$ xxx.xx"

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("\nDepósito\n")
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.\n")
        else:
            print("\nNão foi possível realizar o depósito. Tente novamente.\n")

    elif opcao == "s":
        print("\nSaque\n")
        valor = float(input("Informe o valor do saque: "))
        if valor > 0 and valor <= saldo and valor <= LIMITE and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.\n")
        else:
            print("\nNão foi possível realizar o saque. Possiveis motivos:\nSaldo insuficiente\nLimite de saques diários alcançado.\nValor do saque maior que o limite.\nValor digitado incorretamente.")

    elif opcao == "e":
        print("\nExtrato\n")
        print(f"{extrato}\n\nSaldo atual: R$ {saldo:.2f}.")

        
    elif opcao == "q":
        print("\nSaindo...")
        break

    else:
        print("\nOpção inválida, por favor selecione novamente a operação desejada.")