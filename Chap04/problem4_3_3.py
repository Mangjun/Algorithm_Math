"""
문제: 이진 탐색법으로 루트 2 계산하기
"""

low = 1
high = 2

while high - low > 0.000001:
    mid = (low + high) / 2
    if mid * mid > 2:
        high = mid
    else:
        low = mid

    print("mid = {:.10f}".format(mid))