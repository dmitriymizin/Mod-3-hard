
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def  calculate_structure_sum(*args):
    sum_ = 0
    for item in args:
        if isinstance(item, list):
            for elem in item:
                sum_ += calculate_structure_sum(elem)
        elif isinstance(item, tuple):
            for elem in item:
                sum_ += calculate_structure_sum(elem)
        elif isinstance(item, set):
            for elem in item:
                sum_ += calculate_structure_sum(elem)
        elif isinstance(item, dict):
            for key, value in item.items():
                sum_ += calculate_structure_sum(key, value)
        elif isinstance(item, str):
            sum_ += len(item)
        elif isinstance(item, int):
            sum_ += item
    return sum_

result = calculate_structure_sum(data_structure)
print(result)

