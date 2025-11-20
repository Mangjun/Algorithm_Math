import sys

"""
문제: N가지의 코인 중 모든 종류의 코인을 모을 때까지 필요한 금액의 기댓값 구하기
조건: 비용은 1달러
"""

def solve(N):
    """
    접근 방식: 코인 수집가의 문제 -> 가짓수 X 비용 X 조화 급수

    Input:
        N: 코인 가짓수
    Return: 금액의 기댓값
    """
    answer = 1

    for i in range(2, N + 1):
        answer += 1 / i
    
    return answer * N

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    print(solve(N))