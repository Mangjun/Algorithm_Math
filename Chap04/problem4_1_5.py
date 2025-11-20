import sys

"""
문제: 2개의 선분이 교차하는지 확인
"""

def solve(A):
    """
    접근 방식: 벡터의 외적

    Case1. 교차
        Condition 1. A와 B가 선분 CD의 각각 반대편에 존재 -> A와 B의 외적의 값이 부호가 반대
        Condition 2. C와 D가 선분 AB의 각각 반대편에 존재 -> C와 D의 외적의 값이 부호가 반대
    Case2. 포함 -> 외적의 값이 0 (특수 케이스라 먼저 비교)
        Condition 1. 점이 선분의 좌표 사이에 존재 -> 포함 성립

    Input:
        A: 점 4개 좌표 리스트
    Return: 교차 여부
    """
    # 벡터화
    VCD = [A[2][0] - A[3][0], A[2][1] - A[3][1]]
    VCA = [A[2][0] - A[0][0], A[2][1] - A[0][1]]
    VCB = [A[2][0] - A[1][0], A[2][1] - A[1][1]]

    VAB = [A[0][0] - A[1][0], A[0][1] - A[1][1]]
    VAC = [A[0][0] - A[2][0], A[0][1] - A[2][1]]
    VAD = [A[0][0] - A[3][0], A[0][1] - A[3][1]]

    # 벡터의 외적 계산 -> 기능으로 분할?
    a_resolve = (VCA[0] * VCD[1] - VCA[1] * VCD[0])
    b_resolve = (VCB[0] * VCD[1] - VCB[1] * VCD[0])
    c_resolve = (VAC[0] * VAB[1] - VAC[1] * VAB[0])
    d_resolve = (VAD[0] * VAB[1] - VAD[1] * VAB[0])

    # Case 2
    if a_resolve == 0:
        if (min(A[2][0], A[3][0]) <= A[0][0] <= max(A[2][0], A[3][0])) and (min(A[2][1], A[3][1]) <= A[0][1] <= max(A[2][1], A[3][1])):
            return True

    if b_resolve == 0:
        if (min(A[2][0], A[3][0]) <= A[1][0] <= max(A[2][0], A[3][0])) and (min(A[2][1], A[3][1]) <= A[1][1] <= max(A[2][1], A[3][1])):
            return True
    
    if c_resolve == 0:
        if (min(A[0][0], A[1][0]) <= A[2][0] <= max(A[0][0], A[1][0])) and (min(A[0][1], A[1][1]) <= A[2][1] <= max(A[0][1], A[1][1])):
            return True
        
    if d_resolve == 0:
        if (min(A[0][0], A[1][0]) <= A[3][0] <= max(A[0][0], A[1][0])) and (min(A[0][1], A[1][1]) <= A[3][1] <= max(A[0][1], A[1][1])):
            return True

    # Case 1
    # Condition 1
    if a_resolve * b_resolve < 0:
        # Condition 2
        if c_resolve * d_resolve < 0:
            return True
        
    return False

if __name__ == '__main__':
    N = 4
    A = []

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().strip().split())
        A.append((x, y))

    if solve(A):
        print('Yes')
    else:
        print('No')