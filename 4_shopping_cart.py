def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

prices_list = [2.99, 8.99, 6.99, 9.99, 11.99]
total = calculate_total(prices_list)
print("Total de compras seria: ", total)
