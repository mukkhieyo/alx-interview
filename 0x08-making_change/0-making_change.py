#!/usr/bin/python3
"""
A function that determines the fewest
number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """returns the fewest number of coins to meet total"""
    if total <= 0:
        return 0

    """Sorting the list of coins in descending order"""
    coins.sort(reverse=True)
    current_total = total
    num_coins = 0

    for coin in coins:
        num = current_total // coin
        num_coins += num
        current_total -= num * coin

    if current_total == 0:
        return num_coins
    else:
        return -1
