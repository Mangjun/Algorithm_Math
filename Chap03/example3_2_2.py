import sys

"""
문제: 최대공약수 구하기
"""

def solve(A, B):
    """
    접근 방식: 유클리드 호제법

    Input: 두 수
    Return: 최대공약수
    """
    return gcd(A, B)
    
def gcd(A, B):
    while A >= 1 and B >= 1:
            if A < B:
                B = B % A
            else:
                A = A % B
        
    if A >= 1:
        return A
    else:
        return B

if __name__ == '__main__':
    A, B = map(int, sys.stdin.readline().strip().split())

    print(solve(A, B))