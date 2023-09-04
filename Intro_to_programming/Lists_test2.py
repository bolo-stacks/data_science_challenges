

# Mostra a porcentagem de pessoas que gostaram do filme.
def percentage_liked(ratings):
    # Converte os números acima de 4 de aprovação em boolean True.
    list_liked = [i >= 4 for i in ratings]
    # Calculo da porcentagem das pessoas que gostaram com rating acima de 4 de 5 max
    percentage_liked = sum(list_liked) / len(list_liked)

    return percentage_liked


res = percentage_liked([1, 2, 5, 4, 5, 1])
print(res)

