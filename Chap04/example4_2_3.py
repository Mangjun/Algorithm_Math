import sys

"""
문제: 눈 시뮬레이션
"""

def solve(N, Q_List):
    """
    접근 방식: 계차를 사용하여 계산

    Step 1. 계차 배열 생성
    Step 2. 질문마다 계차 배열 업데이트
    Step 3. 계차가 부호에 따라 문자열 출력 -> 양수일 시 <, 음수일 시 >, 0일 시 =

    Input:
        N: 지역 수
        Q_List: 눈 리스트
    Return: 인접한 지역 간의 눈 양
    """

    answer = ''

    # Step 1
    N_List = [ 0 ] * N

    # Step 2
    for q in Q_List:
        N_List[(q[0] - 1)] += q[2]
        if q[1] < N:
            N_List[q[1]] -= q[2]
    
    # Step 3
    for i in range(1, N):
        if N_List[i] > 0:
            answer += '<'
        elif N_List[i] == 0:
            answer += '='
        else:
            answer += '>'
    
    return answer

if __name__ == '__main__':
    N, Q = map(int, sys.stdin.readline().strip().split())

    Q_List = []
    for _ in range(Q):
        L, R, X = map(int, sys.stdin.readline().strip().split())
        Q_List.append((L, R, X))

    print(solve(N, Q_List))