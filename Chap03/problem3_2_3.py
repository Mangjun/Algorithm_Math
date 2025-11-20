import sys

"""
문제: N개의 양의 정수의 최소공배수 구하기
"""

def solve(N, A):
    """
    접근 방식: 유클리드 호제법 & 최소공배수와 최대공약수의 관계

    Input:
        N: 양의 정수 수
        A: 양의 정수 리스트
    Return: 최소공배수
    """
    answer = 0

    for i in range(N - 1):
        if i == 0:
            answer = lcm(A[i], A[i + 1], gcd(A[i], A[i + 1]))
        else:
            answer = lcm(answer, A[i + 1], gcd(answer, A[i + 1]))

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
    
def lcm(A, B, gcd):
    """
    Input:
        A, B: 양의 정수
        gcd: 최대공약수
    Return: 최소공배수
    """
    return A * B // gcd

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    print(solve(N, A))