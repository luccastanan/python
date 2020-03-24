class Calculadora:

    def soma(self, num1, num2):
        return num1 + num2
    
    def subtracao(self, num1, num2):
        return num1 - num2

    def multiplicacao(self, num1, num2):
        return num1 * num2

    def divisao(self, num1, num2):
        return num1 / num2

valor1 = float(input('Digite o 1º valor: '))
valor2 = float(input('Digite o 2º valor: '))

calc = Calculadora()
resSoma = calc.soma(valor1, valor2)
resSub = calc.subtracao(valor1, valor2)
resMul = calc.multiplicacao(valor1, valor2)
resDiv = calc.divisao(valor1, valor2)

print('Soma: ' + str(resSoma))
print('Subtração: ' + str(resSub))
print('Multiplicação: ' + str(resMul))
print('Divisão: ' + str(resDiv))

# int = número inteiro
# float = número fracionado
# str = string = palavra