import sys

"""
문제: 입장 인원 계산하기
"""

def solve(A, Q_List):
    """
    접근 방식: 누적합 배열

    Step 1. 누적합 배열 생성
    Step 2. 질문별 계산

    Input:
        A: 날짜별 입장 인원 리스트
        Q_List: 질문 리스트
    Return: 질문별 인원수 합계
    """

    # Step 1
    Sum_List = []
    Sum_List.append(A[0])

    for i in range(1, len(A)):
        Sum_List.append(Sum_List[i - 1] + A[i])

    # Step 2
    for q in Q_List:
        if (q[0] == 1):
            print(Sum_List[q[1] - 1])
        else:
            print(Sum_List[q[1] - 1] - Sum_List[q[0] - 2])

if __name__ == '__main__':
    N, Q = map(int, sys.stdin.readline().strip().split())
    A = list(map(int, sys.stdin.readline().strip().split()))

    Q_List = []
    for _ in range(Q):
        L, R = map(int, sys.stdin.readline().strip().split())
        Q_List.append((L, R))

    solve(A, Q_List)