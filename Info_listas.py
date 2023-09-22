l = [15, 5, 7] # Criando nova lista

print(l) # Exibindo a lista inteira
print(l[0]) # Exibindo o valor na posição 0 da lista

for i in range(len(l)):
    print(l[i]) # Exibe cada valor de i em relação ao tamanho da lista (a função len é utilizado para pegar o tamanho da lista)

l.append(1) # Adiciona um termo no final da lista
print(l)

l.insert(2, 'a') # Adiciona um termo na posição especifica na lista
print(l)

l.pop(2) # Remove um valor em determinada posição da lista
print(l)

l.remove(5) # Compara os valores da lista com o informado e caso ele existe o remove independente da posição
print(l)