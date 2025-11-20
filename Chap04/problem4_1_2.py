import sys
import math

"""
문제: N개의 점에서 가장 가까운 두 점의 거리를 구하기
"""

def solve(A):
    """
    접근 방식: 분할 정복법을 사용

    Step 1. x좌표, y좌표 기준으로 정렬하기
    Step 2. x좌표로 정렬된 리스트를 중간값으로 경계선을 두어 왼쪽과 오른쪽끼리 최단 거리 구하기
    Step 3. 경계선과 x의 좌표의 거리가 최단 거리보다 작은 값만 추리기
    Step 4. y좌표 기준으로 좌표들끼리 최단 거리 갱신하기

    Input:
        A: N개의 점 좌표 리스트
    Return: 최단 거리
    """

    answer = 0

    # Step 1
    Px = sorted(A, key=lambda item: item[0])
    Py = sorted(A, key=lambda item: item[1])

    # Step 2
    answer = _solve_recursive(Px, Py)

    # math.sqrt는 느린 함수이므로 마지막 한번만 계산
    return math.sqrt(answer)

def brute_force_search(Px):
    length = len(Px)
    
    min_value = math.inf

    for i in range(length - 1):
        for j in range(i + 1, length):
            min_value = min(min_value, (Px[j][0] - Px[i][0]) ** 2 + (Px[j][1] - Px[i][1]) ** 2)

    return min_value
            

def _solve_recursive(Px, Py):
    length = len(Px)

    # 리스트의 길이가 3보다 작을 시 모든 좌표 비교
    if length <= 3:
        return brute_force_search(Px)
    
    # 중간값 경계로 나누기
    middle = length // 2
    Left_Px = Px[0:middle]
    Right_Px = Px[middle:]

    # Py도 미리 분류
    Left_Py = []
    Right_Py = []

    Left_Px_set = set(Left_Px)

    for p in Py:
        if p in Left_Px_set:
            Left_Py.append(p)
        else:
            Right_Py.append(p)

    delta = min(_solve_recursive(Left_Px, Left_Py), _solve_recursive(Right_Px, Right_Py))

    # Step 3
    Strip = []
    middle_x = Px[middle][0]

    for p in Py:
        if (p[0] - middle_x) ** 2 < delta:
            Strip.append(p)

    # Step 4
    strip_len = len(Strip)

    for i in range(strip_len - 1):
        for j in range(i + 1, strip_len):
            if (Strip[i][1] - Strip[j][1]) ** 2 < delta:
                delta = min(delta, (Strip[i][0] - Strip[j][0]) ** 2 + (Strip[i][1] - Strip[j][1]) ** 2)
            else:
                break

    return delta

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    A = []

    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())

        A.append((a, b))

    print(solve(A))