menu = """
===========JACK'S BANK============
----------Seja Bem-Vindo!---------

===>Selecione a opção desejada<===
    (s) Sacar
    (d) Depositar
    (e) Extrato
    (q) Sair

==================================
"""
mensagem_final = "\nMuito obrigado por utilizar o Jack' Bank!"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        while True:
            try:
                valor = float(input("Informe o valor a ser depositado: R$"))
            except ValueError as str:
                print("\nOperação inválida! Utilize apenas números.\n")
            else:
                break
        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito no valor de R$ {valor:.2f}"
            print("\nDepósito realizado com sucesso!")

        else: print("Valor informado é inválido")



    elif opcao == "e":
        print("===========JACK'S BANK============")
        print("   \n==========EXTRATO==========    ")
        print("Não houve movimentação" if not extrato else extrato)
        print(f"\nSaldo R${valor:.2f}")
        print("\n   ===========================   ")

    elif opcao == "s":
        print("Saque")
        while True:
            try:
                saque = float(input("Digite o valor desejado: R$"))
            except ValueError as str:
                print("\nOperação inválida! Utilize apenas números.\n")
            else:
                break
        saldo_insuficiente = saque > saldo
        limite_excedido = saque > limite
        limite_diario = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("\nOperação não realizada. Saldo insuficiente :/")
        elif limite_excedido:
            print("\nLimite por saque (R$500) excedido")
        elif limite_diario:
            print("\nLimite diário de saques excedido. Volte amanhã ;)")
        
        else:
            print("\nSaque no valor de R$", saque, "realizado com sucesso!")
            numero_saques += 1
            saldo -= saque
            extrato += f"\nSaque no valor de R$ {saque:.2f}"




    elif opcao == "q":
        print(mensagem_final)
        break

    else:
        print("Opção inválida. Tente novamente.")