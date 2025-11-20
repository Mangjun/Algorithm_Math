import sys

"""
문제: 자신의 나이가 소수인지 판별
"""

def solve(Age):
    """
    Input:
        Age: 나이
    Return: 소수 여부
    """

    if Age > 2 and Age % 2 == 0:
        return False

    LIMIT = int(Age ** 0.5)

    for i in range(2, LIMIT + 1):
        if Age % i == 0:
            return False
    
    return True

if __name__ == '__main__':
    Age = int(sys.stdin.readline().strip())

    print(solve(Age))