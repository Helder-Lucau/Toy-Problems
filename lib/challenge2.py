# Two numbers are positive

def positive_numbers(a, b, c):
    num = 0

    if a > 0:
        num += 1
    if b > 0:
        num += 1
    if c > 0:
        num += 1
    if num == 2:
        print (True)
    else:
        print (False)

# Examples
positive_numbers(2, 4, -3)
# positive_numbers(-4, 6, 8)
# positive_numbers(4, -6, 9)
# positive_numbers(-4, 6, 0)
# positive_numbers(4, 6, 10)
# positive_numbers(-14, -3, -4)