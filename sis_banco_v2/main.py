from classes import Cliente,Banco

cliente = Cliente(value = 1000)
banco = Banco()
opt = 0
while (opt != '4'):
    opt = input("Selecione a opção desejada: ")
    match (opt):
        case '1':
            value = input("Insira a quantia a ser depositada: ")
            print(banco.deposito(cliente, float(value)))
        case '2':
            value = input("Insira a quantia a ser sacada: ")
            print(banco.saque(cliente, float(value)))
        case '3':
            banco.extrato(cliente)
        case _:
            print("Escolha inválida.")

print("Finalizando.")