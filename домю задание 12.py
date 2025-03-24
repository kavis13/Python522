def rect_paral(a, b, c):
    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


print(rect_paral(2, 4, 6))
print(rect_paral(5, 8, 2))
print(rect_paral(1, 6, 8))


#########################################################


def rect_paral1(a, b, c):
    global s

    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))


s = 0
print(rect_paral1(2, 4, 6))
print(s)
print(rect_paral1(5, 8, 2))
print(s)
print(rect_paral1(1, 6, 8))
print(s)


###########################################################

def rect_paral2(a, b, c):
    s = 0

    def inner(i, j):
        nonlocal s
        s += i * j

    inner(a, b)
    inner(a, b)
    inner(a, b)
    s = 2 * s
    return s


print(rect_paral2(2, 4, 6))
print(rect_paral2(5, 8, 2))
print(rect_paral2(1, 6, 8))

############################################################
