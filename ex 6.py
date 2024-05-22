# ENTRADA
# dois numeros aleatorios
# qual operação deseja utilizar

# Saida
# resultado no formato num1 op num2 = resultado

num1 = float(input("Digite o primeiro numero "))
num2 = float(input("Digite o segundo numero "))
op = str(input("Qual a operação desejada? ( +  -  *  /  )  "))


def soma(x, y):
    return x + y


def subtrai(x, y):
    return x - y


def multiplica(x, y):
    return x * y


def divide(x, y):
    return x / y


operacoes = {
    '+': (soma, '+'),
    '-': (subtrai, '-'),
    '*': (multiplica, '*'),
    '/': (divide, '/')
}

func,operacao = operacoes[op]
resultado = func(num1,num2)

print(resultado)
"""operacoes = {
    '+': (lambda x, y: x + y, '/'),
    '-': (lambda x, y: x - y, '/'),
    '*': (lambda x, y: x * y, '/'),
    '/': (lambda x, y: x / y, '/')
}

func,operador = operacoes[op]
resultado = func(num1,num2)
print(resultado)"""

"""if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == "*":
    resultado = num1 * num2
elif op == "/":
    resultado = num1 / num2
else:
    op = "Erro"
if op == "Erro":
    print("Erro")
else:
    print(f"{num1}{op}{num2}={resultado}")"""
