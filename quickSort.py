
def partition(array, low, high):

  # função para encontrar a posição da partição
  pivot = array[high]

  # ponteiro para elemento maior
  i = low - 1

  # percorrer todos os elementos
  # compara cada elemento com o pivô
  for j in range(low, high):
    if array[j] <= pivot:
      # se o elemento menor que o pivô for encontrado
      # troque-o pelo maior elemento apontado por i
      i = i + 1

      # trocando elemento em i com elemento em j
      (array[i], array[j]) = (array[j], array[i])

  # troque o elemento pivô pelo elemento maior especificado por i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # retornar a posição de onde a partição é feita
  return i + 1

# função para executar quicksort
def quickSort(array, low, high):
  if low < high:

    # encontre o elemento pivô tal que
    # elemento menor que o pivô está à esquerda
    # elemento maior que o pivô está à direita
    pi = partition(array, low, high)

    # chamada recursiva à esquerda do pivô
    quickSort(array, low, pi - 1)

    # chamada recursiva à direita do pivô
    quickSort(array, pi + 1, high)


degrau = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(degrau)

size = len(degrau)

quickSort(degrau, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(degrau)