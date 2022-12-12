def SelectionSort(array, size):

   # for percorrendo o degrau para busca do menor valor
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
         
            if array[i] < array[min_idx]:   #para classificar em ordem decrescente, altere > para < nesta linha
                min_idx = i  # seleciona o elemento mínimo em cada loop
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


degrau = [21, 32, 23, 12, 65]
size = len(degrau)
SelectionSort(degrau, size)
print('Sorted Array in Ascending Order:')
print(degrau)