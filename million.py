num = 1000000

is_not_zero = True
iterated = 0

while is_not_zero:
    num //= 2
    iterated += 1
    if num == 0:
        is_not_zero = False

print(iterated)
