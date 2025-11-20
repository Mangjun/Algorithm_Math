import sys

"""
문제: 자연수 N을 소인수분해
시간 복잡도: O(√n)
"""

def solve(N):
    """
    참고: 제곱근을 구하는 것은 느리므로 제곱으로 바꿔 생각

    Input:
        N: 자연수
    Return: 소인수분해 결과 리스트
    """
    if N <= 3:
        return [N]

    divisors = []

    i = 2
    while i * i <= N:
        if (N % i == 0):
            divisors.append(i)
            N = N // i
        else:
            i += 1
        
    if (N > 1):
        divisors.append(N)

    return divisors

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    for d in solve(N):
        print(d, end=' ')