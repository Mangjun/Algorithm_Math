import sys

"""
문제: 편집 거리
조건:
    1. 한 문자 제거
    2. 한 문자 추가
    3. 한 문자를 변경
"""

def solve(S, T):
    """
    접근 방식: 동적 계획법

    Step 1. DP 배열 생성
    Step 2. 첫줄 값 초기화 -> 서로 길이가 다를 때
    Step 3. 최소값 구하기

    Condition 1. 제거
    Condition 2. 추가
    Condition 3. 변경

    Input:
        S: 바꿀 문자열
        T: 문자열
    Return: 최소 조작 횟수
    """
    h = len(S)
    w = len(T)

    # Step 1
    dp = [[0] * (w + 1) for _ in range(h + 1)]

    # Step 2
    for i in range(1, h + 1):
        dp[i][0] = i

    for j in range(1, w + 1):
        dp[0][j] = j

    # Step 3
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

    return dp[h][w]

if __name__ == '__main__':
    S = str(sys.stdin.readline().strip())
    T = str(sys.stdin.readline().strip())

    print(solve(S, T))