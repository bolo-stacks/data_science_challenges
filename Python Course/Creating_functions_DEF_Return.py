"""
Criar uma função com o comando def - return
"""


def least_difference(a, b, c):
    """
    Você chamou o help na função criada least_difference
    --→ Ela encontra a menor diferença entre 3 números
    subtraíndo um do outro e retornando o menor.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


# Testando a nossa nova função:
print(least_difference(8, 5, 3),
      least_difference(1, 10, 100),
      least_difference(1, 10, 10),
      least_difference(5, 6, 7))

'''
Se nós quisermos que a função help responda o que a função
least_difference faz é necessário inserir um texto 
descritivo dentro da função.
'''

help(least_difference)


# Mais um exemplo de uso da criação de uma função.

def greet(who="Colin"):
    print("Hello,", who)


greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")


# Mais exemplos: funções dentro de funções...(higher-order functions)

def mult_by_five(x):
    return 5 * x


def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)


def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))


print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n')  # '\n' is the newline character - it starts a new line


# Exemplo de higher order function (função dentro de função).

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5


print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n', )
