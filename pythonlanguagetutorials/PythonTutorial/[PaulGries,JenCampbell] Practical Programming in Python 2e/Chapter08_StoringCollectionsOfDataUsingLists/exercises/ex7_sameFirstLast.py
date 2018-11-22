
def sameFirstLast(list):
    # precondition: len(list) >= 2
    return list[0] == list[-1]


assert sameFirstLast([1,2,1])
assert sameFirstLast([1])
assert not sameFirstLast([3, 4, 5, 6])
# error if passed []