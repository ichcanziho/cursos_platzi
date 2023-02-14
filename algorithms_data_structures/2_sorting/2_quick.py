from random import sample, seed


def quick_sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        print("L", izquierda, "C", centro, "R", derecha)
        return quick_sort(izquierda) + centro + quick_sort(derecha)
    else:
        return lista


if __name__ == '__main__':
    seed(1)
    simple_array = sample(range(1, 11), 9)
    print("original:", simple_array)
    print("*"*24)
    simple_array = quick_sort(simple_array)
    print("*" * 24)
    print("ordered:", simple_array)
