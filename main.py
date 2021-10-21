from utils.calculator import calculadora

novaSoma = calculadora()
valorAntigo = 0
sair = False

while sair == True:
    operador = input('Digite o operador: ')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print()
    
    while n1>9 and n1<0:
        print('Número invalido, insira de 0 a 9')
        n1 = int(input('Digite o primeiro número: '))

    while n2>9 and n2<0:
        print('Número invalido, insira de 0 a 9')
        n2 = int(input('Digite o segundo número: '))

    novaSoma = calculadora.calculo(n1, n2, operador)
    print(novaSoma)