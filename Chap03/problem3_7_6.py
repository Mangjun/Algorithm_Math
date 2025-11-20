import sys

"""
문제: 여름 방학 N일 동안 공부량의 최댓값
조건:
    1. 2일 연속으로 공부 X
"""

def solve(N, A):
    """
    접근 방식: 동적 계획법

    Input:
        N: 여름 방학 일수
        A: 공부량 리스트
    """

    dp = [0] * (N + 1)
    dp[1] = A[0]

    for i in range(2, N + 1):
        value = A[i - 1]
        dp[i] = max(dp[i - 2] + value, dp[i - 1])

    return dp[N]

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    if len(A) == N:
        print(solve(N, A))