data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

res = 0


def sum_list(list_):

    global res

    for i in list_:
        if isinstance(i, int):
            res += i
        elif isinstance(i, str):
            res += len(i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            sum_list(i)
        elif isinstance(i, dict):
            for j in i:
                if isinstance(j, int):
                    res += j
                elif isinstance(j, str):
                    res += len(j)
                else:
                    sum_list(j)
                if isinstance(i[j], int):
                    res += i[j]
                elif isinstance(i[j], str):
                    res += len(i[j])
                else:
                    sum_list(i[j])


    return res

x = sum_list(data_structure)
print(x)
