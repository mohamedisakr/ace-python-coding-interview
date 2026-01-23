from typing import List


def coin_change_greedy_dict(money, coins):
    """
    Greedy algorithm for coin change.
    money: integer amount to change
    coins: list of denominations in decreasing order
    Returns: dictionary {coin: count}
    """
    result = {}
    while money > 0:
        for coin in coins:
            if coin <= money:
                result[coin] = result.get(coin, 0) + 1
                money -= coin
                break
    return result


def coin_change_greedy_list(money, coins):
    """
    Greedy algorithm for coin change.
    money: integer amount to change
    coins: list of denominations in decreasing order
    Returns: dictionary {coin: count}
    """
    result = []
    while money > 0:
        for coin in coins:
            if coin <= money:
                result.append(coin)
                money -= coin
                break
    return result


def coin_change_greedy_trace(money, coins):
    result = {}
    step = 1
    while money > 0:
        for coin in coins:
            if coin <= money:
                result[coin] = result.get(coin, 0) + 1
                print(f"Step {step}: take {coin}, remaining = {money - coin}")
                money -= coin
                step += 1
                break
    return result

# Run the trace
# coin_change_greedy_trace(77, [25, 10, 5, 1])


def coin_change_fast(money, coins):
    """
    Faster version using division instead of looping coin by coin.
    money: integer amount to change
    coins: list of denominations in decreasing order
    Returns: dictionary {coin: count}
    """
    result = {}
    amount = money
    for coin in coins:
        count = amount // coin
        result[coin] = count
        amount -= coin * count
    return result


amount = 77
denominations = [25, 10, 5, 1]
print(coin_change_fast(amount, denominations))
