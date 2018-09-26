import random

def three_steps(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    memo = [-1] * (n+1)
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[i]


def main():
    print(three_steps(5))

if __name__ == "__main__":
    main()

