from functools import reduce

numbers = [485, 635]
Compare_numbers = reduce(lambda x, y: x if (x > y) else y, numbers)

print(Compare_numbers)