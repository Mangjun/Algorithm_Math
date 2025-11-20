import sys

"""
문제: 베낭 문제
"""

def solve(N, W, N_List):
    """
    접근 방식: 동적 계획법

    Step 1. dp 1차원 배열 생성 -> 이전 인덱스만 참조하므로 2차원 배열이 필요없음
    Step 2. Condition 비교 후 최댓값 구하기

    Input:
        N: 물건 수
        W: 무게 제한
        N_List: (무게, 가치) 리스트
    Return: 가치의 최댓값
    """

    dp = [0] * (W + 1)

    for i in range(1, N + 1):
        w = N_List[i - 1][0]
        v = N_List[i - 1][1]
        for j in range(W, w - 1, -1):
            dp[j] = max(dp[j - w] + v, dp[j])
    
    return dp[W]

if __name__ == '__main__':
    N, W = map(int, sys.stdin.readline().strip().split())

    N_List = []
    for i in range(N):
        w, v = map(int, sys.stdin.readline().strip().split())
        N_List.append((w, v))

    print(solve(N, W, N_List))