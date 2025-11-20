import sys

"""
문제: N장의 카드에서 합이 100000이 되는 2장의 카드를 선택하는 경우의 수 구하기
"""

def solve(N, A):
    """
    접근 방식: 투 포인터

    Step 1. 정렬
    Step 2. 투 포인터 방식을 사용

    Condition 1. left와 right의 값이 같을 때 -> 조합 사용
    Condition 2. 같은 수가 반복된다면?(left와 right의 값이 다를 때) -> 같은 수만큼 계산해서 경우의 수 구하고 더하기

    Input:
        N: 카드 수
        A: 카드 값 리스트
    Return: 경우의 수
    """
    card_sum = 100000
    answer = 0

    # Step 1
    sort_list = sorted(A)

    # Step 2
    left = 0
    right = N - 1

    while left < right:
        left_value = sort_list[left]
        right_value = sort_list[right]

        if left_value + right_value < card_sum:
            left += 1
        elif left_value + right_value == card_sum:
            # Condition 1
            if left_value == right_value:
                answer += ((right - left + 1) * (right - left) // 2)
                break
            # Condition 2
            else:
                left_point = left
                while left_value == sort_list[left_point]:
                    left_point += 1

                right_point = right
                while right_value == sort_list[right_point]:
                    right_point -= 1

                answer += (left_point - left) * (right - right_point)

                left = left_point
                right = right_point
        else:
            right -= 1

    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    if len(A) == N:
        print(solve(N, A))