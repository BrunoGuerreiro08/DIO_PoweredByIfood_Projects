from classes import Banco

def mostrarMenu():
    print('''
1. Deposito
2. Saque
3. Emitir extrato
4. Adicionar cliente
5. Adicionar conta
6. Sair da aplicação
        ''')

pessoas = []
banco = Banco()

opt = 0
while (opt != '6'):
    mostrarMenu()
    opt = input("Selecione a opção desejada: ")
    match (opt):
        case '1':
            cpf = input("Insira o cpf do cliente: ")
            if banco.listarContas(cpf, pessoas):
                infos = {'nConta': input("Insira o número da conta: "), 'value': float(input("Insira a quantia a ser depositada: "))}
                print(banco.deposito(infos))
        case '2':
            cpf = input("Insira o cpf do cliente: ")
            if banco.listarContas(cpf, pessoas):
                infos = {'nConta': input("Insira o número da conta: "), 'value': float(input("Insira a quantia a ser sacada: "))}
                print(banco.saque(infos))
        case '3':
            cpf = input("Insira o cpf do cliente: ")
            if banco.listarContas(cpf, pessoas):
                infos = input("Insira o número da conta: ")
                banco.extrato(infos)
        case '4':
            cpf = input("Insira o cpf do cliente: ")
            pessoas.append(banco.addCliente(cpf, pessoas))
            pass
        case '5':
            cpf = input("Insira o cpf do cliente: ")
            print(banco.addConta(cpf, pessoas))
        case '6':
            pass
        case _:
            print("Escolha inválida.")

print("Finalizando.")