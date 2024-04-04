menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"
            print("Seu depósito foi concluído. Verifique seu extrato!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe quanto deseja sacar: "))

        excede_saldo = valor > saldo

        excede_limite = valor > limite

        excede_saques = numero_saques >= LIMITE_SAQUES

        if excede_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")

        elif excede_limite:
            print("Operação falhou! O valor do saque ultrapassa limite diário.")

        elif excede_saques:
            print("Operação falhou! Você excedeu o limite de saques diários.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f} \n"
            numero_saques += 1
            print("Saque autorizado! Retire seu dinheiro.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ===================")
        print("Não foram realizadas transações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
