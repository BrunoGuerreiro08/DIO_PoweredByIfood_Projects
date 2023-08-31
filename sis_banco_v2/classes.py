class Conta:
    value = 0.0
    nSaques = 3
    extrato = []

    def __init__(self, cliente, nConta):
        self.agencia = 0001
        self.nConta = nConta

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
    conta = []

    def deposito(self, cliente, value):
        cliente.setSaldo(value)
        cliente.addExtrato(value)
        return "Operação concluída com sucesso"

    def saque(self, cliente, value):
        if (value > 500.0):
            return "A quantia solicitada execede o limite permitido para saques."

        if (cliente.nSaques == 0):
            return "O cliente estourou a quantidade de saques diários permitida."            

        if (value > cliente.saldo):
            return "A quantia requisitada excede o saldo em conta."
        
        cliente.setSaldo(-1 * value)
        cliente.setNSaques(-1)
        cliente.addExtrato(-1 * value)
        return "Operação concluída com sucesso"
    
    def extrato(self, cliente):
        print("|----- EXTRATO -----|")
        for entry in cliente.getExtrato():
            if (entry < 0):
                print(f"- R$ {float(-1 * entry):.2f}", end= "\n")
            else:
                print(f"  R$ {float(entry):.2f}", end= "\n")

        print("|----- TOTAL -----|")
        print(f"  R$ {float(cliente.getSaldo()):.2f}", end= "\n")