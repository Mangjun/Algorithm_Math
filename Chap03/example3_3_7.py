import sys

"""
문제: N개의 카드 중 같은 색의 카드를 선택하는 가짓수 계산하기
"""

def solve(N, A):
    """
    Step 1. 색깔별 카드 개수 세기
    Step 2. 경우의 수 구하기

    Input:
        N: 카드 수
        A: 카드 색 리스트
    Return: 경우의 수
    """
    num_check_list = [0, 0, 0, 0] # 카드 수 체크용 리스트
    for i in range(N):
        num_check_list[A[i]] += 1

    return combination(A[1], 2) + combination(A[2], 2) + combination(A[3], 2)

def combination(n, r):
    """
    Input:
        n: 전체 수
        r: 선택 수
    Return: 경우의 수
    """
    return factorial(n - r + 1, n) // factorial(1, r)

def factorial(start, end):
    """
    Input:
        start: 시작 숫자
        end: 끝 숫자
    Return: 곱한 값
    """
    if start == end:
        return start

    answer = start
    for i in range(start + 1, end + 1):
        answer *= i
    
    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    print(solve(N, A))