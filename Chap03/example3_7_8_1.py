import sys

"""
문제: 베낭 문제
"""

def solve(N, W, N_List):
    """
    접근 방식: 동적 계획법

    Step 1. dp 2차원 배열 생성 -> 매우 비효율적(슬라이딩 윈도우 채택)
    Step 2. Condition 비교 후 최댓값 구하기
    
    Condition 1. 가방에 공간 여부 확인
    Condition 1-1. 물건을 넣는다
    Condition 1-2. 물건을 넣지 않는다

    Input:
        N: 물건 수
        W: 무게 제한
        N_List: (무게, 가치) 리스트
    Return: 가치의 최댓값
    """

    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        w = N_List[i - 1][0]
        v = N_List[i - 1][1]
        for j in range(0, W + 1):
            # Condition 1.
            if j - w < 0:
                # Condition 1-2
                dp[i][j] = dp[i - 1][j]
            else:
                # Condition 1-1
                c1 = dp[i - 1][j - w] + v
                # Condition 1-2
                c2 = dp[i - 1][j]
                dp[i][j] = max(c1, c2)
    
    return dp[N][W]

if __name__ == '__main__':
    N, W = map(int, sys.stdin.readline().strip().split())

    N_List = []
    for i in range(N):
        w, v = map(int, sys.stdin.readline().strip().split())
        N_List.append((w, v))

    print(solve(N, W, N_List))