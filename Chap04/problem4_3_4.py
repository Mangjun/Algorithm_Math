"""
문제: 사칙 연산만으로 10^0.3 근삿값 계산하기
"""

low = 1
high = 2

while high - low > 0.00000001:
    mid = (high + low) / 2

    temp = mid
    for i in range(9):
        temp = temp * mid

    if temp > 1000:
        high = mid
    else:
        low = mid

    print("mid = {:.12f}".format(mid))