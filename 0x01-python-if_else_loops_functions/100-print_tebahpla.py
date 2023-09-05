#!/usr/bin/python3
for i in range(0, 26):
    c = ord('z') - i
    if i % 2 == 1:
        c = (chr(c - ord('a') + ord('A')))
    else:
        c = chr(c)
    print("{}".format(c), end='')

# alternative method: (a bit lazy, lol)
# for i in 'zYxWvUtSrQpOnMlKjIhGfEdCbA':
# print("{}".format(i), end="")
# or
# for c in range(122, 96, -1):
# if c % 2 != 0:
# c = (c - 32)
# print("{}".format(chr(c)), end="")
