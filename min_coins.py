import random

def min_coins(coins, val):
    memo = dict()
    for coin in coins:
        memo[coin] = 1
    memo[0] = 0
    return min_coins_helper(coins, val, memo)

def min_coins_helper(coins, val, memo):
    if val in memo:
        return memo[val]
    else:
        min_count = float('inf')
        for coin in coins:
            if val - coin >= 0:
                curr_count = 1 + min_coins_helper(coins, val-coin, memo)
                if curr_count < min_count:
                    min_count = curr_count
        memo[val] = min_count
        return min_count

def n_ways(coins, val):
    memo = dict()
    memo[0] = 1
    memo[1] = 1
    memo[5] = 2
    memo[10] = 4
    memo[25] = 13
    return n_ways_helper(coins, val, memo)

def n_ways_helper(coins, val, memo):
    if val in memo:
        return memo[val]
    else:
        count = 0
        for coin in coins:
            if val - coin >= 0:
                count += n_ways_helper(coins, val-coin, memo)
        memo[val] = count
        return count


def main():
    coins = [1, 5, 10, 25]
    val = 7
    print(min_coins(coins, val))
    print(n_ways(coins, val))

if __name__ == "__main__":
    main()

