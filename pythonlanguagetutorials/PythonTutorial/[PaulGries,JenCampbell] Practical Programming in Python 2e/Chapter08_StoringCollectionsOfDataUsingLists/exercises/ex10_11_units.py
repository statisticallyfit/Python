units = [["km", "miles", "league"], ["kg", "pound", "stone"]]
# a
print(units[0])
# b
print(units[1])
# c
print(units[0][0])
# d
print(units[1][0])
# e
print(units[0][1:])
# f
print(units[1][0:2], "\n\n")

# negative indices
# a
print(units[-2])
# b
print(units[-1])
# c
print(units[-2][-3])
# d
print(units[-1][-3])
# e
print(units[-2][-2:])
# f
print(units[-1][:-1])
print(units[-1][-3:-1])