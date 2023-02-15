def greedy_change(coin_set, n):
    solution = []
    suma = 0
    iteration = 1
    while suma < n:
        # La mejor opción greedy será tomar la moneda de más alta denominación
        best_option = max(coin_set)
        # A tu vuelto, sumale la moneda de más alta denominación
        suma += best_option
        # Mientras NO hayas llegado al número que te pidieron
        if suma <= n:
            # Añade la moneda de más alto valor al la lista de vuelto
            solution.append(best_option)
            print(iteration, solution)
            iteration += 1
        # Si te pasaste entonces:
        else:
            # ignora la última suma que hayas hecho
            suma -= best_option
            # Remueve la "best_option" del set de monedas disponibles
            coin_set.remove(best_option)
    return solution


if __name__ == '__main__':
    coins = [5, 2, 1]
    n = 23
    print("your current budget is:", n)
    print("the coins allowed for change are:", coins)
    print("*"*24)
    ans = greedy_change(coins, n)
    print("*" * 24)
    print("Your change is:", ans)
