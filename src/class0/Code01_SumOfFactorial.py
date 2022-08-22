"""
@author: jackchen
给定整数N，返回1！+ 2！+ ... +N!
"""


def calSumOfFactorial(n):
    factor = 1
    factor_sum = 0
    if n<=0:
        return factor_sum
    else:
        for i in range(1, n+1):
            factor = factor * idq
            factor_sum = factor_sum+factor
        return factor_sum


if __name__ == '__main__':
    res = calSumOfFactorial(4)
    print(res)

