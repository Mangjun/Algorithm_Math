import sys

"""
문제: 여행 총 거리 계산하기
시간 복잡도: O(N+M)
"""

def solve(N, A, M, B_List):
    """
    접근 방식: 누적합 배열 사용

    Step 1. 누적합 배열 생성
    Step 2. 누적합 배열을 이용해 총 이동 거리 계산
    
    Input:
        N: 역 수
        A: 각 역마다의 거리 리스트
        M: 이동 수
        B_List: 이동 경로 리스트
    Return: 총 이동 거리
    """
    answer = 0

    # Step 1.
    N_List = [ 0 ]
    for i in range(N - 1):
        N_List.append(N_List[i] + A[i])

    # Step 2.
    for i in range(1, M):
        answer += abs(N_List[B_List[i - 1] - 1] - N_List[B_List[i] - 1])

    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())

    B_List = []
    for _ in range(M):
        B = int(sys.stdin.readline().strip())
        B_List.append(B)

    print(solve(N, A, M, B_List))