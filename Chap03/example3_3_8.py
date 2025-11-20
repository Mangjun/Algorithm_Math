import sys

"""
문제: N개의 카드 중 5장을 선택하여 합이 1000이 되는 경우의 수 구하기
"""

def solve(N, A):
    """
    접근 방식: 동적 계획법

    Step 1. 정렬 -> 약간의 속도를 올릴 가능성이 존재
    Step 2. DP 테이블 준비
    Step 3. 계산

    Input:
        N: 카드 수
        A: 카드 값 리스트
    Return: 경우의 수
    """
    card_sum = 1000
    card_cnt = 5

    # Step 1
    sort_list = sorted(A)

    # Step 2
    dp = [[0] * (card_sum + 1) for _ in range(card_cnt + 1)]
    dp[0][0] = 1

    # Step 3
    for card in sort_list:
        for cnt in range(card_cnt, 0, -1):
            for sum in range(card_sum, card - 1, -1):
                dp[cnt][sum] += dp[cnt - 1][sum - card]

    return dp[card_cnt][card_sum]

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    if len(A) == N:
        print(solve(N, A))