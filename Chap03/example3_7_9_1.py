import sys

"""
문제: 부분합 문제
"""

def solve(N, S, A):
    """
    접근 방식: 동적 계획법

    Input:
        N: 정수 갯수
        S: 합
        A: 정수 값 리스트
    Return: 합을 만들 수 있는 지
    """

    dp = [False] * (S + 1)
    dp[0] = True

    for i in range(1, N + 1):
        value = A[i - 1]
        for j in range(S, value - 1,-1):
            if dp[j - value]:
                dp[j] = True

    return dp[S]

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    S = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    if len(A) == N:
        print(solve(N, S, A))