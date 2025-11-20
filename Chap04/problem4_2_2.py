import sys

"""
문제: 각 시간마다 편의점에 있는 종업원의 수 계산
시간 복잡도: O(N+T)
"""

def solve(T, N, N_List):
    """
    접근 방식: 계차 배열

    Step 1. 계차 배열 생성
    Step 2. 계차 배열을 이용해 계산

    Input:
        T: 편의점 문 닫는 시간
        N: 종업원 수
        N_List: 종업원 영업시간 리스트 (시작 시간, 종료 시간)
    Return: 각 시간마다 종업원 수
    """
    # Step 1
    T_List = [ 0 ] * (T + 1)
    
    for i in range(N):
        T_List[N_List[i][0]] += 1
        T_List[N_List[i][1]] -= 1

    # Step 2
    answer = 0
    for i in range(T):
        answer = answer + T_List[i]
        print(answer)

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())

    N_List = []
    for _ in range(N):
        L, R = map(int, sys.stdin.readline().strip().split())
        N_List.append((L, R))

    solve(T, N, N_List)