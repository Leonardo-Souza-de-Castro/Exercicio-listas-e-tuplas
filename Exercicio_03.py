lista = []

for i in range(10):
    a = int(input("Digite um valor: "))

    lista.insert(i, a)


lista.sort()
print(lista)
print(f"O maior valor é {lista[9]} e seu indice é 9")