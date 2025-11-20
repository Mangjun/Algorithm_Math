import sys

"""
문제: N개의 양의 정수의 최대공약수 구하기
"""

def solve(N, A):
    """
    접근 방식: 유클리드 호제법

    Input:
        N: 양의 정수 수
        A: 양의 정수 리스트
    Return: 최대공약수
    """
    answer = 0

    for i in range(N - 1):
        if i == 0:
            answer = gcd(A[i], A[i + 1])
        else:
            answer = gcd(answer, A[i + 1])

    return answer

def gcd(A, B):
    """
    Input: 두 수
    Return: 최대공약수
    """
    while A >= 1 and B >= 1:
        if A > B:
            A = A % B
        else:
            B = B % A
    
    if A >= 1:
        return A
    else:
        return B

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    print(solve(N, A))