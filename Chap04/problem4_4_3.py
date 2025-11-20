import sys

"""
문제: 양의 정수 N의 약수 개수를 f(x)라고 할 때, ∑(i=1, N)i X f(i)를 구해라
시간 복잡도: O(NlogN)
"""

def solve(N):
    """
    Input:
        N: 양의 정수
    Return: ∑(i=1, N)i X f(i)
    """
    answer = 0
    for i in range(1, N + 1):
        k = N // i

        answer += i * (k * (k + 1) // 2)

    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    print(solve(N))