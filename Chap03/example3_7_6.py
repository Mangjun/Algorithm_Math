import sys

"""
문제: 개구리의 이동
"""

def solve(N, H):
    """
    접근 방식: 동적 계획법

    Condition 1. 1칸 이동
    Condition 2. 2칸 이동
    
    Input:
        N: 발판 수
        H: 발판 높이 값 리스트
    Return: 이동 거리 최솟값
    """
    dp = [None] * (N + 1)
    dp[0] = 0
    dp[1] = 0

    for i in range(2, N + 1):
        if i == 2:
            dp[i] = abs(H[i - 2] - H[i - 1])
        if i >= 3:
            # Condition 1
            c1 = dp[i - 1] + abs(H[i - 2] - H[i - 1])
            # Condition 2
            c2 = dp[i - 2] + abs(H[i - 3] - H[i - 1])

            dp[i] = min(c1, c2)

    return dp[N]

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    H = list(map(int, sys.stdin.readline().strip().split()))

    print(solve(N, H))