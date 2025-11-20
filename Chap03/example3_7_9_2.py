import sys
import math

"""
문제: 코인 문제
"""

def solve(N, S, A):
    """
    접근 방식: 동적 계획법

    Input:
        N: 동전 종류 수
        S: 지불해야할 돈
        A: 동전 값 리스트
    Return: 필요한 동전의 최솟값
    """

    dp = [math.inf] * (S + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        value = A[i - 1]
        for j in range(value, S + 1):
            dp[j] = min(dp[j], dp[j - value] + 1)

    if dp[S] == math.inf:
        return -1
    return dp[S]

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    S = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    if len(A) == N:
        print(solve(N, S, A))