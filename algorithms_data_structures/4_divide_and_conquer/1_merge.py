from random import sample, seed


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        print(f"Dividing left: {left} right {right}")

        merge_sort(left)
        merge_sort(right)
        # Esta es una de las dudas que me surgió al intentar entender recursividad.
        print("¿Cuándo se ejecuta esta línea?")

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        print(f'comparando izquierda {left}, derecha {right}')
        print(arr)
        print('-' * 50)

    return arr


if __name__ == '__main__':
    n = 8
    seed(1)
    array = sample(range(0, 101), n)
    print("original array:", array)
    print('-' * 20)
    ordered_arr = merge_sort(array)
    print('-' * 20)
    print("ordered array:", ordered_arr)
