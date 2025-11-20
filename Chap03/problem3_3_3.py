import sys

"""
문제: nCr 구하기
"""

def solve(n, r):
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
    n, r = map(int, sys.stdin.readline().strip().split())

    print(solve(n, r))