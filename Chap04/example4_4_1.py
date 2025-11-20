import sys

"""
문제: N 이하의 소수 모두 출력
"""

def solve(N):
    """
    접근 방식: 에라토스테네스의 체

    Input:
        N: 자연수
    Return: N 이하의 모든 소수
    """
    prime = [True] * (N + 1)

    Limit = int(N ** 0.5)
    
    for i in range(2, Limit + 1):
        if prime[i]:
            for j in range(2 * i, N + 1, i):
                prime[j] = False
    
    for i in range(2, N + 1):
        if prime[i]:
            print(i, end=' ')
    print()

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    solve(N)