class calculadora():  
    def __init__(self, valorAnterior=0):
        self.valorAnterior = valorAnterior

    def limparValorAnterior(self):
        self.valorAnterior = 0

    def calculo(n1, n2, operador):
        if operador == '+':
            return n1+n2
        elif operador == '-':
            return n1-n2
        elif operador == '*':
            return n1*n2
        elif operador == '/':
            return n1/n2
        else:
            return 'VALOR INVÁLIDO'
