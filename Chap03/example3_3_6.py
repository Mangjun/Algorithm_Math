import sys

"""
문제: N개의 물건 중 제한된 총 합계 금액을 넘지 않는 서로 다른 물건 2개를 구매
"""

def solve(N, A, Limit):
    """
    접근 방식: 투 포인터 방식

    Step 1. 가격 순으로 정렬
    Step 2. 투 포인터 방식

    Input:
        N: 물건 수
        A: 물건 가격 리스트
        Limit: 제한된 금액
    Return: 경우의 수
    """
    answer = 0

    # Step 1
    sort_list = sorted(A)

    # Step 2
    left = 0
    right = N - 1

    while left < right:
        if sort_list[left] + sort_list[right] <= Limit:
            answer += right - left
            left += 1
        else:
            right -= 1

    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    print(solve(N, A, 500))