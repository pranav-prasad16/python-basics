def sum_all(*args):
    result = 0
    for i in args:
        result += i
    return result
    # return sum(args)

print(sum_all())
print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))