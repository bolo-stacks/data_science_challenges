"""Para representar os mesmos dados em uma lista Python.
Para criar uma lista, você precisa usar colchetes ([, ]) e
separar cada item com uma vírgula. Cada item na lista é uma
cadeia de caracteres Python, portanto, cada um é colocado entre aspas."""

flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold",
                "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print("\nImprime todos os ítens da lista: ", flowers_list)
print("Imprime o tipo da variável: ", type(flowers_list))
print('Imprime o numero de ítens da lista: ', len(flowers_list))
print("Primeiro ítem da lista: ", flowers_list[0])
print("Segundo ítem da lista: ", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Imprime o décimo ítem da lista: ", flowers_list[9])

# Utilizando cortes com o print e variável list
print("Primeiros tres ítens: ", flowers_list[:3])
print("Últimos dois ítens: ", flowers_list[-2:])

# Remover ítens da lista
flowers_list.remove("globe thistle")
print("Imprime a lista após remoção de ítem (globe thistle): ", flowers_list)

# Adiciona ítem (snapdragon)
flowers_list.append("snapdragon")
print('Imprime lista após adição de ítem (snapdragon): ', flowers_list)

# Listas com Int
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
print("Número de ítens da lista:", len(hardcover_sales))
print("Ítem nº 2:", hardcover_sales[1])

# Imprime o menor e o maior número
print("Menor:", min(hardcover_sales))
print("Maior:", max(hardcover_sales))

# Soma todos os ítens da lista
print("Soma os números da lista:", sum(hardcover_sales))

# Cálculos com ítens utilizando o slice
print("Média dos últimos cinco ítens:", sum(hardcover_sales[:5])/5)
