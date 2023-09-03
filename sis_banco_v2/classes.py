import random

class Cliente:
    contas = []
    
    def __init__(self, infos):
        self.cpf = infos['cpf']
        self.nome = infos['nome']
        self.end = infos['end']
        self.dataNasc = infos['dataNasc']

    def addConta(self, conta):
        self.contas.append(conta)
        return f"Conta conta registrada no cpf {self.cpf}"
    
    def listarContas(self):
        for conta in self.contas:
            print(conta)

class Conta:
    saldo = 0.0
    nSaques = 3
    extrato = []

    def __init__(self, cliente, nConta):
        self.agencia = '0001'
        self.nConta = nConta
        self.cliente = cliente

    def __str__(self):
        return f'''
Agência:{self.agencia}
Numero da conta:{self.nConta}
Saldo: R${self.saldo:.2f}
Numero de saques restantes: {self.nSaques}'''

    def getSaldo(self):
        return(str(self.saldo))
    
    def setSaldo(self, value):
        self.saldo += value
    
    def getNSaques(self):
        return (str(self.nSaques))
    
    def setNSaques(self, value):
        self.nSaques += value

    def addExtrato(self, value):
        self.extrato.append(value)
    
    def getExtrato(self):
        return self.extrato
    
class Banco:
    contas = []

    def deposito(self, infos):
        contaID = self.validarConta(infos['nConta'])
        if not contaID:
            return f"Conta inválida."
        
        contaID.setSaldo(infos['value'])
        contaID.addExtrato(infos['value'])
        return "Operação concluída com sucesso"

    def saque(self, infos):
        contaID = self.validarConta(infos['nConta'])
        if not contaID:
            return f"Conta inválida."
        
        if (infos['value'] > 500.0):
            return "A quantia solicitada execede o limite permitido para saques."

        if (contaID.nSaques == 0):
            return "A conta estourou a quantidade de saques diários permitida."            

        if (infos['value'] > contaID.getSaldo()):
            return "A quantia requisitada excede o saldo em conta."
        
        contaID.setSaldo(-1 * infos['value'])
        contaID.setNSaques(-1)
        contaID.addExtrato(-1 * infos['value'])
        return "Operação concluída com sucesso"
    
    def extrato(self, infos):
        contaID = self.validarConta(infos)
        if not contaID:
            print("Conta inválida.")
            return
        
        print("|----- EXTRATO -----|")
        for entry in contaID.getExtrato():
            if (entry < 0):
                print(f"- R$ {float(-1 * entry):.2f}", end= "\n")
            else:
                print(f"  R$ {float(entry):.2f}", end= "\n")

        print("|----- TOTAL -----|")
        print(f"  R$ {float(contaID.getSaldo()):.2f}", end= "\n")

    def addCliente(self, cpf, clientes):
        clienteID = self.validarCPF(cpf, clientes)
        if clienteID:
            return f"CPF já cadastrado."
        
        infos = {'cpf': cpf, 'nome': input("Informe o nome: "), 'end': input("Informe o endereço: "), 'dataNasc': input("Informe a data de nascimento: ")}
        print("Cliente cadastrado com sucesso.")
        return Cliente(infos)

    def addConta(self, cpf, clientes):
        clienteID = self.validarCPF(cpf, clientes)
        if not clienteID:
            return f"CPF inválido."
        conta = Conta(clienteID, self.gerarNConta())
        self.contas.append(conta)
        return clienteID.addConta(conta)
    
    def validarCPF(self, cpf, clientes):
        for cliente in clientes:
            if (cpf == cliente.cpf):
                return cliente
        
        return False
    
    def validarConta(self, nConta):
        for conta in self.contas:
            if (nConta == conta.nConta):
                return conta
        
        return False
    
    def gerarNConta(self):
        return str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    
    def listarContas(self, cpf, clientes):
        clienteID = self.validarCPF(cpf, clientes)
        if not clienteID:
            print ("CPF inválido.")
            return False
        
        clienteID.listarContas()
        return True