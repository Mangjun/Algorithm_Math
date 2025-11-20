"""
문제: [0, 1] 2x^2dx 정적분의 근삿값을 구하기
"""

start = 0
end = 1
N = 1000

def func(x):
    return 2 * (x ** 2)

area = 0
dx = (end - start) / N

for i in range(N):
    x = start + i * dx
    area += (func(x) + func(x + dx)) / 2

print(area * dx)