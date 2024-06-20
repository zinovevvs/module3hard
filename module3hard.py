
def count_numbers(*args):
    count = 0
    for i in args:
        if isinstance(i, int):
            count += i
        elif isinstance(i, str):
            count += len(i)
        elif isinstance(i, dict):
            count += count_numbers(*i.items())
        elif isinstance(i, (list, tuple, set)):
            count += count_numbers(*i)
    return count


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = count_numbers(data_structure)
print(result)