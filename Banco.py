import os
saques_disponiveis = 3
saldo = 0
extrato = ''

################# MENUS ####################

menu_start = """
    ====================================================
    ================== Banco Dolabella =================
    ==================================================== 
    ================= Escolha uma opção ================
    ====================================================

    [1] Depositar
    [2] Sacar (Saques Disponíveis: {})
    [3] Extrato Bancário
    [4] Sair

    ====================================================
"""
    ####

menu_depositar = """
    ====================================================
    ================== Banco Dolabella =================
    ==================================================== 
    ===================== Depositar ====================
    ====================================================

              Insira um valor para depositar...
              Digite [v] para Voltar.

    ====================================================
"""
    ####

menu_sacar = """
    ====================================================
    ================== Banco Dolabella =================
    ==================================================== 
    ===================== Depositar ====================
    ====================================================

        Insira um valor para sacar até (R$ 500.00)...
        Saques disponíveis ({})
        Digite [v] para Voltar.

    ====================================================
"""
    ###

menu_extrato = """
    ====================================================
    ================== Banco Dolabella =================
    ==================================================== 
    ===================== Extrato ====================
    ====================================================
        Extrato:

{}

        Saldo Atual: {:.2f}
        Digite [v] para Voltar.

    ====================================================
"""

###############   FUNCTIONS   ######################

def Depositar():
    global saldo, extrato
    os.system('cls')
    while True:
        print(menu_depositar)
        valor = input('Insira: ')
        if valor == 'v':
            break
        elif valor[0] not in '1234567890':
            os.system('cls')
            print('insira um valor Válido.')
        elif float(valor) <= 0:
            os.system('cls')
            print('insira um valor Válido.')
        else:
            saldo += float(valor)
            os.system('cls')
            print(f'Novo Saldo: R$ {saldo:.2f}')
            extrato += f'          Deposito: R$ {float(valor):.2f}\n'
            
def Sacar():
    global saldo, saques_disponiveis, extrato
    os.system('cls')
    while True:
        print(menu_sacar.format(saques_disponiveis))
        valor = input('Insira: ')
        if valor == 'v':
            break
        elif saques_disponiveis == 0:
            os.system('cls')
            print('Sem Saques disponíveis.')
        elif valor[0] not in '1234567890':
            os.system('cls')
            print('insira um valor Válido.')
        elif float(valor) <= 0:
            os.system('cls')
            print('insira um valor Válido.')
        elif float(valor) > 500:
            os.system('cls')
            print('insira um valor abaixo de R$ 500.00.')
        elif float(valor) > saldo:
            os.system('cls')
            print('insira um valor abaixo do seu saldo Atual')
        else:
            saldo -= float(valor)
            os.system('cls')
            print(f'Novo Saldo: R$ {saldo:.2f}')   
            saques_disponiveis -= 1 
            extrato += f'          Saque: R$ {float(valor):.2f}\n'

def Extrato():
    os.system('cls')
    while True:
        print(menu_extrato.format(extrato if extrato != '' else '          Sem Nenhuma operação...' , saldo))
        valor = input('Insira: ')
        if valor == 'v':
            break
        else:
            print('Insira um valor válido')

def Start():
    global saques_disponiveis
    while True:
        os.system('cls')
        print(menu_start.format(saques_disponiveis))
        opcao = input("Digite a opção: ")
        if opcao not in '1234567890':
            print('Insira um valor de opção valido.')
        elif int(opcao) == 1:
            os.system('cls')
            Depositar()
        elif int(opcao) == 2:
            Sacar()
        elif int(opcao) == 3:
            Extrato()
        elif int(opcao) == 4:
            print('Sair')
            break
        else:
            print('Insira um valor de opção valido.')

##############################################################

Start()
