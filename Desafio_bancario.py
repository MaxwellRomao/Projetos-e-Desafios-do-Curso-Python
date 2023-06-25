menu = """

===== Digite sua Opção =======
                            
 [d] -> Depositar           
 [s] -> Sacar               
 [e] -> Extrato             
 [q] -> Sair  

==============================

Entre com sua Opção: => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            print(f" => O Valor de {valor}, foi depositado com sucesso!! ")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("==>> Operação falhou! O valor informado é inválido.")

    elif opcao == "s":

        print(f"\n >> Seu aldo é: R$ {saldo}")  # Mostra o saldo assim que é escolhido a opção saque

        if saldo == 0:
            print("==> Não é possível realizar saque!.")
            
        
        valor = float(input("\nInforme o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("==> Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("==> Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("==> Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

            print(f">> O saque no valor de: {valor}, foi realizado com sucesso!.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n*************** EXTRATO *****************")
        print("Sem movimentações realizadas." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("*****************************************")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")