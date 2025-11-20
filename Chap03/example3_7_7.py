import sys

"""
문제: 계단을 오르는 방법
"""

def solve(N):
    """
    접근 방식: 동적 계획법

    Input:
        N: 계단 수
    Return: 방법 수
    """
    dp = [None] * (N + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[N]

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    print(solve(N))