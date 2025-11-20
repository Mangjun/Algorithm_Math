import sys

"""
문제: 병합 정렬
"""

def MergeSort(A):
    if len(A) <= 1:
        return A
    
    m = len(A) // 2
    A_Dash = MergeSort(A[0:m])
    B_Dash = MergeSort(A[m:])

    c1 = 0
    c2 = 0
    C = []

    while (c1 < len(A_Dash) or c2 < len(B_Dash)):
        if c1 == len(A_Dash):
            # 배열 'A'가 비어있는 경우
            C.append(B_Dash[c2])
            c2 += 1
        elif c2 == len(B_Dash):
            # 배열 'B'가 비어있는 경우
            C.append(A_Dash[c1])
            c1 += 1
        else:
            # 비어있지 않은 경우
            if A_Dash[c1] <= B_Dash[c2]:
                C.append(A_Dash[c1])
                c1 += 1
            else:
                C.append(B_Dash[c2])
                c2 += 1

    return C

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    for e in MergeSort(A):
        print(e, end=' ')