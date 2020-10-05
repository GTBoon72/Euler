from typing import List
import numpy as np

def numberOfCoinCombinations(amount: int, coins: List[int]):
    if not amount > 0:
        raise ValueError("amount should be an integer higher than 0")
    if not all(x>0 for x in coins):
        raise ValueError("only positive integers larger than 0 are allowed in this list")
    if not len(coins)==len(np.unique(coins)):
        raise ValueError("only unique coins are allowed as input")

    #Didn't think this solution up myself. Found the code here:
    #https://www.rosettacode.org/wiki/Count_the_coins#Simple_version
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]

def main():
    print("The number of English coin combinations adding up to 2 pound, equals: " +
        str(numberOfCoinCombinations(200, [1, 2, 5, 10, 20, 50, 100, 200])))

if __name__ == '__main__':
    main()