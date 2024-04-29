LIMITE = 500
LIMITE_SAQUES = 3
saldo = 0
extrato = "\n"
numero_saques = 0

menu = """
 ===== MENU =====

  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair
  => """

while True:

    opcao = input(menu)

    if opcao == "d":
        print("\n ===== DEPÓSITO =====\n")
        valor = input(" Informe o valor do depósito: ")

        try:
            valor = float(valor)
            if valor > 0:
                saldo += valor
                extrato += f" Depósito: R$ {valor:.2f}\n"
                print(f"\n Depósito de R$ {valor:.2f} realizado com sucesso.\n")
            else:
                print("\n Não foi possível realizar o depósito. Tente novamente.\n")
        except:
            print(" Valor digitado incorretamente.")

            
    elif opcao == "s":
        print("\n ===== SAQUE =====\n")
        valor = input(" Informe o valor do saque: ")

        try:
            valor = float(valor)
            if valor > 0 and valor <= saldo and valor <= LIMITE and numero_saques < LIMITE_SAQUES:
                saldo -= valor
                extrato += f" Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"\n Saque de R$ {valor:.2f} realizado com sucesso.\n")
            else:
                print("\n Não foi possível realizar o saque. Possiveis motivos:\n Saldo insuficiente\n Limite de saques diários alcançado.\n Valor do saque maior que o limite.\n Valor digitado incorretamente.")
        except:
            print(" Valor digitado incorretamente.")


    elif opcao == "e":
        print("\n ===== EXTRATO =====")
        if extrato:
            print(f" {extrato}\n\n Saldo atual: R$ {saldo}.")
        else:
            print(f" Nenhuma operação foi realizada.\n\n Saldo atual: R$ {saldo}.")

        
    elif opcao == "q":
        print("\n Saindo...")
        break

    else:
        print("\n Opção inválida, por favor selecione novamente a operação desejada.")