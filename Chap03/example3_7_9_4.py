import sys
import bisect

"""
문제: 가중치 구간 스케줄링 문제
"""

def solve(N, A):
    """
    접근 방식: 동적 계획법

    Step 1. DP 배열을 생성
    Step 2. 종료 시간 오름차순 정렬
    Step 3. 최댓값 구하기

    Condition 1. 안고른다
    Condition 2. 고른다

    Input:
        N: 일 수
        A: (시작 시간, 종료 시간, 보수) 리스트
    Return: 보수의 최댓값
    """

    # Step 1
    dp = [0] * (N + 1)

    # Step 2
    sort_list = sorted(A, key=lambda x: x[1])
    end_times = [x[1] for x in sort_list]

    # Step 3
    for i in range(1, N + 1):
        start_time = sort_list[i - 1][0]
        end_time = sort_list[i - 1][1]
        value = sort_list[i - 1][2]
        # Condition 1
        c1 = dp[i - 1]
        # Condition 2
        k = bisect.bisect_right(end_times, start_time)

        if k > 0:
            c2 = dp[k] + value
        else:
            c2 = 0 + value

        dp[i] = max(c1, c2)
    
    return dp[N]

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    
    A = []
    for i in range(N):
        S, E, V = map(int, sys.stdin.readline().strip().split())
        A.append((S, E, V))
    
    print(solve(N, A))
