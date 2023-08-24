"""
Calcular o valor da casa de acordo como numero
de quartos, banheiros e se tem ou não porão
"""


def get_expected_cost(beds, baths, has_basement):
    value = 80000 + (beds * 30000) + (baths * 10000) + (40000 * has_basement)
    return value


option_one = get_expected_cost(1, 1, False)
option_two = get_expected_cost(2, 1, True)

print(option_one)
print(option_two)

# testando soma de booleans
print('verdadeiro + verdadeiro + verdadeiro + verdadeiro =', True + True + True + True)
print('Falso + falso =', False + False)
print('verdadeiro + falso =', True + False)
print('verdadeiro + verdadeiro + falso =', True + True + False)
