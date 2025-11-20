r = 2.0
a = 2.0
repeats = 5

for i in range(1, repeats + 1):
    x, y = a, a * a

    a = 2.0 * x
    b = y - a * x

    next_a = (r - b) / a
    print("Step #{}: a = {:.12f} -> {:.12f}".format(i, a, next_a))
    a = next_a