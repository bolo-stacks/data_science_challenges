"""
Custo da gravação na jóia
anel de ouro laminado = $50, $7 por caractere gravado
anel de ouro sólido = $100, $10 por caractere gravado
espaços e pontuação são cobrados
custo do projeto de acordo com um texto
"""


def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = solid_gold * 100 + (len(engraving) * 10)
    else:
        cost = solid_gold + 50 + (len(engraving) * 7)
    return cost


engraved_cost = cost_of_project('2', False)
print('o custo total do seu anel gravado é R$', engraved_cost)

project_one = cost_of_project("Charlie+Denver", True)
print("o custo do projeto_one é R$", project_one)

project_two = cost_of_project('08/10/2000', False)
print('o custo do projeto_dois é R$', project_two)
