import os

################# MENUS ####################

menu_start = """
    ====================================================
    ================== Banco Dolabella =================
    ==================================================== 
    ================= Escolha uma opção ================
    ====================================================
    [1] Criar Usuario
    [2] Criar Conta Corrente
    [3] Depositar
    [4] Sacar (Saques Disponíveis: {})
    [5] Extrato Bancário
    [6] Listar Contas
    [7] Sair

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
    ###
menu_criar_usuario = """
    ====================================================
    ================== Banco Dolabella =================
    ==================================================== 
    ================= Escolha uma opção ================
    ====================================================

        Digite [n] criar novo Usuário.

        Digite [v] para Voltar.

    ====================================================
"""
    ###
menu_criar_conta = """
    ====================================================
    ================== Banco Dolabella =================
    ==================================================== 
    ================= Escolha uma opção ================
    ====================================================

        Digite [n] criar nova Conta.

        Digite [v] para Voltar.

    ====================================================
"""
    ###
menu_conta = """
    ====================================================
    ================== Banco Dolabella =================
    ==================================================== 
    ================= Escolha uma opção ================
    ====================================================

        Contas:
{}

        Digite [v] para Voltar.

    ====================================================
"""

###############   FUNCTIONS   ######################
def Listar_Contas(contas):
   os.system('cls')
   lista_contas = ''
   for conta in contas:
       lista_contas += f"""\
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        
        """
   while True:
       print(menu_conta.format(lista_contas))
       valor = input('Insira um valor: ')
       if valor != 'v':
           os.system('cls')
           print('Valor Inválido.')
       else:
           break

def Criar_Conta(usuarios, agencia, conta):
    os.system('cls')
    numero_conta = len(conta) + 1
    while True:
        print(menu_criar_conta)
        valor = input('Insira uma opção: ')
        if valor == 'v' :
            break
        elif valor not in 'vn':
            os.system('cls')
            print('Insira um valor entre as opções válidas.')
        else:
            
            cpf = input('Informe o CPF: ')
            usuario = Filtrar_Usuario(cpf, usuarios)
            if not usuario:
                os.system('cls')
                print('Usuário não encontrado.')
            else:
                os.system('cls')
                conta.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
                print(f'Conta criada com Sucesso em nome de {usuario["nome"]}!')
    return conta

def Filtrar_Usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def Criar_Usuario(usuarios):
    os.system('cls')
    while True:
        print(menu_criar_usuario)
        valor = input('Insira uma opção: ')
        if valor == 'v' :
            break
        elif valor not in 'vn':
            os.system('cls')
            print('Insira um valor entre as opções válidas.')
        else:
            
            cpf = input('Informe o CPF: ')
            usuario = Filtrar_Usuario(cpf, usuarios)
            if usuario:
                os.system('cls')
                print('Esse CPF já foi Utilizado.')
            else:
                nome = input("Informe o nome completo: ")
                data_nascimento = input("Informe a data de nascimento [dd-mm-aaaa]: ")
                endereco = input("Informe o endereço [logradouro, nro - bairro - cidade/sigla estado]: ")

                usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
                os.system('cls')
                print(f'Usuário {nome} criado com Sucesso!')
    return usuarios

def Depositar(saldo, extrato,/):
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
    return saldo, extrato
            
def Sacar(*,saldo, extrato, limite):
    os.system('cls')
    while True:
        print(menu_sacar.format(limite))
        valor = input('Insira: ')
        if valor == 'v':
            break
        elif limite == 0:
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
            limite -= 1 
            extrato += f'          Saque: R$ {float(valor):.2f}\n'
    return saldo, extrato, limite

def Extrato(saldo,/,*,extrato):
    os.system('cls')
    while True:
        print(menu_extrato.format(extrato if extrato != '' else '          Sem Nenhuma operação...' , saldo))
        valor = input('Insira: ')
        if valor == 'v':
            break
        else:
            print('Insira um valor válido')

def Start():
    saques_limite = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    saldo = 0
    extrato = ''

    while True:
        os.system('cls')
        print(menu_start.format(saques_limite))
        opcao = input("Digite a opção: ")
        if opcao[0] not in '1234567890':
            print('Insira um valor de opção valido.')
        elif int(opcao) == 1:
            Criar_Usuario(usuarios)
        elif int(opcao) == 2:
            Criar_Conta(usuarios, AGENCIA, contas)
        elif int(opcao) == 3:
            saldo, extrato = Depositar(saldo,extrato)
        elif int(opcao) == 4:
            saldo, extrato, saques_limite = Sacar(
                saldo=saldo,
                limite=saques_limite,
                extrato=extrato
            )
        elif int(opcao) == 5:
            Extrato(saldo, extrato= extrato)
        elif int(opcao) == 6:
            Listar_Contas(contas)
        elif int(opcao) == 7:
            print('Sair')
            break
        else:
            print('Insira um valor de opção valido.')

##############################################################

Start()
