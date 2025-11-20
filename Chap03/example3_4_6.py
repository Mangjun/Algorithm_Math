import sys

"""
문제: 시험에서 모든 객관식 문제 찍을 때 점수의 기댓값 구하기
"""

def solve(N, Q_List):
    """
    Input:
        N: 문제 수
        Q_List: (선택지 수, 배점) 리스트
    Return: 점수의 기댓값
    """
    answer = 0

    for q in Q_List:
        answer += (q[1] // q[0])
    
    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    Q_List = []
    for i in range(N):
        P, Q = map(int, sys.stdin.readline().strip().split())
        Q_List.append((P, Q))

    print(solve(N, Q_List))