import sys
import math

"""
문제: 점 A와 선분 BC의 최단 거리 구하기
"""

def solve(ax, ay, bx, by, cx, cy):
    """
    접근: 벡터 내적과 각의 관계를 이용

    Case 1. 벡터 BA와 벡터 BC의 내적 <= 0, 각 ABC는 둔각(직각)이므로 선분 AB가 최단 거리
    Case 2. 벡터 CA와 벡터 CB의 내적 <= 0, 각 ACB는 둔각(직각)이므로 선분 AC가 최단 거리
    Case 3. 둘 다 만족하지 않을 시 점 A에서 선분 BC의 수선의 발이 최단 거리 -> 벡터 BA와 벡터 BC의 외적(평행사변형의 넓이) / 선분 BC

    Input: 각 점의 좌표
    Return: 최단 거리
    """
    answer = 0

    # 벡터화
    VBA = [ax - bx, ay - by]
    VBC = [cx - bx, cy - by]
    VCA = [ax - cx, ay - cy]
    VCB = [bx - cx, by - cy]

    # Case 1
    if ((VBA[0] * VBC[0] + VBA[1] * VBC[1]) <= 0):
        answer = math.sqrt(VBA[0] ** 2 + VBA[1] ** 2)
    # Case 2
    elif ((VCA[0] * VCB[0] + VCA[1] * VCB[1]) <= 0):
        answer = math.sqrt(VCA[0] ** 2 + VCA[1] ** 2)
    # Case 3
    else:
        answer = abs((VBA[0] * VBC[1] - VBA[1] * VBC[0])) / math.sqrt(VCB[0] ** 2 + VCB[1] ** 2)

    return answer  

if __name__ == '__main__':
    ax, ay = map(int, sys.stdin.readline().strip().split())
    bx, by = map(int, sys.stdin.readline().strip().split())
    cx, cy = map(int, sys.stdin.readline().strip().split())

    print(solve(ax, ay, bx, by, cx, cy))