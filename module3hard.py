
def count_numbers(*args):
    count = 0
    for elem in args:
        if isinstance(elem, int):
            count += 1
        elif isinstance(elem, str):
            count += len(elem)
        elif isinstance(elem, (list, tuple, dict)):
            count += count_numbers(*elem)
    return count


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = count_numbers(data_structure)
print(result)