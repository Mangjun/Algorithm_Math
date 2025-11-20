import sys

"""
문제: 2개의 주사위를 동시에 던졌을 때, 나오는 눈의 합계만큼의 상금이 주어지는데 상금의 기댓값 구하기
"""

def solve(N, B, R):
    """
    Input:
        N: 주사위 면 개수
        B: 주사위1 값 리스트
        R: 주사위2 값 리스트
    Return: 상금의 기댓값
    """
    answer = 0

    for i in range(N):
        answer += B[i] // N
        answer += R[i] // N

    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    B = list(map(int, sys.stdin.readline().strip().split()))
    R = list(map(int, sys.stdin.readline().strip().split()))

    if len(B) == N and len(R) == N:
        print(solve(N, B, R))