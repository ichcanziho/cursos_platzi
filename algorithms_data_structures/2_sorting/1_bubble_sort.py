from random import sample, seed


def bubble_sort(array):
    iteration = 1
    n = len(array)
    for i in range(n-1):
        is_ordered = True
        for j in range(n-1):
            left, right = array[j], array[j+1]
            if right < left:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_ordered = False
            iteration += 1
            print(iteration, array)
        if is_ordered:
            break
    return array


if __name__ == '__main__':
    seed(1)
    simple_array = sample(range(1, 11), 5)
    print("original:", simple_array)
    print("*"*24)
    simple_array = bubble_sort(simple_array)
    print("*" * 24)
    print("ordered:", simple_array)
