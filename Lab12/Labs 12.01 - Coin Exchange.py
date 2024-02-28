"""KKK"""
from json import loads

def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def coin_exchange(amount, data):
    """coin exchange"""
    data = convert_key(loads(data))
    coin_values = sorted(data.keys(), reverse=True)
    remaining_amount = amount
    coin_used = 0
    result = {}

    for value in coin_values:
        if value not in result:
            result[value] = 0
        if remaining_amount <= 0:
            break
        if value <= remaining_amount and data[value] > 0:
            coin_count = min(remaining_amount // int(value), data[value])
            result[value] = coin_count
            remaining_amount -= int(value) * coin_count
            coin_used += coin_count

    if remaining_amount > 0:
        print("Coins are not enough.")
    else:
        print("Amount:", amount)
        print("Coin exchange result:")
        for coin, count in result.items():
            print(" ", coin, "baht =", count, "coins")
        print("Number of coins:", coin_used)

coin_exchange(int(input()), str(input()))
