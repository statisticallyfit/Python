def recurse(n, s):
    if n == 0:
        print(n, s)
    else:
        recurse(n - 1, n + s)

recurse(3, 0)
recurse(4, 0)
recurse(5, 9)
recurse(10, 4)

print("\n")
recurse(0, 1)
recurse(1, 0)
recurse(0, 0)

#recurse(-1, 3) note overflow
recurse(3, -1)
# recurse(-1, 0) # note overflow : rule if n < 0 then we overflow because there is no stop.
# recurse(-3, -3) # note overflow