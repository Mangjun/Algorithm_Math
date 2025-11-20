import sys

"""
문제: 2개의 원의 위치 관계를 출력

위치 관계:
    1. 한 원이 다른 원을 완전히 포함하며, 두 원이 접하지 않는 경우
    2. 한 원이 다른 원을 완전히 포함하며, 두 원이 접하는 경우
    3. 두 원이 서로 교차하는 경우
    4. 두 원 내부에 공통 부분이 없지만, 두 원이 접하는 경우
    5. 두 원 내부에 공통 부분이 없으며, 두 원이 접하지도 않는 경우
"""

def solve(C1, C2):
    """
    접근 방식: 반지름과 중심 간의 거리 이용

    Step 1. 중심 거리와 반지름 차이의 제곱을 구한다
    Step 2. 각 Case를 구한다
        Case 1. 한 원이 다른 원을 완전히 포함하며, 두 원이 접하지 않는 경우 -> |r1 - r2| > d
        Case 2. 한 원이 다른 원을 완전히 포함하며, 두 원이 접하는 경우 -> 내접 관계 |r1 - r2| = d
        Case 3. 두 원이 서로 교차하는 경우 -> 나머지 경우
        Case 4. 두 원 내부에 공통 부분이 없지만, 두 원이 접하는 경우 -> 외접 관계 r1 + r2 = d
        Case 5. 두 원 내부에 공통 부분이 없으며, 두 원이 접하지도 않는 경우 -> r1 + r2 < d

    Input:
        C1: 원 중심 좌표와 반지름
        C2: 원 중심 좌표와 반지름
    Return: 위치 관계
    """

    d = (C1[0] - C2[0]) ** 2 + (C1[1] - C2[1]) ** 2
    r_diff = (C1[2] - C2[2]) ** 2
    r_sum = (C1[2] + C2[2]) ** 2

    pattern = 0

    if (r_diff > d):
        pattern = 1
    elif (r_diff == d):
        pattern = 2
    elif (r_sum == d):
        pattern = 4
    elif (r_sum < d):
        pattern = 5
    else:
        pattern = 3

    return pattern

if __name__ == '__main__':
    C1 = list(map(int, sys.stdin.readline().strip().split()))
    C2 = list(map(int, sys.stdin.readline().strip().split()))

    print(solve(C1, C2))