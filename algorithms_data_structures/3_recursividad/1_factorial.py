from time import time


def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n - 1)


def iterative_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


def main(n):
    start = time()
    recursivo = recursive_factorial(n)
    print(f"recursive time: {time() - start}, value = {recursivo}")
    iterativo = iterative_factorial(n)
    start = time()
    print(f"iterative time: {time() - start}, value = {iterativo}")


if __name__ == '__main__':
    k = 50
    main(k)
