import sys
import math

"""
문제: H시 M분일 때 시침과 분침의 끝 사이의 거리를 구하기
"""

def solve(A, B, H, M):
    """
    접근 방식: 벡터의 차

    Step 1. 12시를 기준으로 두기 (0)
    Step 2. 분침부터 도를 계산 -> 1분당 6
    Step 3. 시침을 계산 + 분침 * 0.5 -> 30도를 60분에 지나가니까 30/60 = 0.5도
    Step 4. 벡터의 차를 계산 -> cos 제 2법칙

    Input:
        A: 시침 길이
        B: 분침 길이
        H: 시
        M: 분
    Return: 시침과 분침의 끝 사이의 거리
    """
    # Step 3
    radian_diff = abs(M * 6 - (((H * 30) % 360) + M * 0.5))

    # Step 4
    answer = A**2 + B**2 - (A * B * 2 * math.cos(math.radians(radian_diff)))

    return math.sqrt(answer)

if __name__ == '__main__':
    A, B, H, M = map(int, sys.stdin.readline().strip().split())

    print(solve(A, B, H, M))