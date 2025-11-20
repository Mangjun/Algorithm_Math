import sys

"""
문제: 여름 방학 N일 동안 공부 시간의 기댓값 구하기
조건:
    1. 주사위를 굴려 눈이 1, 2가 나올 때 A[i]시간 공부
    2. 주사위를 굴려 눈이 3, 4, 5, 6이 나올 때 B[i]시간 공부
"""

def solve(N, A, B):
    """
    Input:
        N: 여름 방학 일 수
        A: 공부 시간 리스트 1
        B: 공부 시간 리스트 2
    Return: 공부 시간의 기댓값
    """
    answer = 0

    for i in range(N):
        answer += (A[i] * 2)
        answer += (B[i] * 4)

    return answer / 6

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    B = list(map(int, sys.stdin.readline().strip().split()))

    if len(A) == N and len(B) == N:
        print(solve(N, A, B))