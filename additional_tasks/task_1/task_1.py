def quicksort_test():
    a = [2, 3, 4, 1, 2, 6, 7]
    b = quicksort(a)
    print(b)
    a = [1, 1, 1, 1, 1, 1, 2, 3, 4, 5]
    b = quicksort(a)
    print(b)
    a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    b = quicksort(a)
    print(b)


def quicksort(list_in):
    if len(list_in) == 0:
        return []
    first_elem = list_in.pop(0)
    if len(list_in) == 0:
        return [first_elem]
    new_list = []
    list_min = list(filter(lambda x: x < first_elem, list_in))
    new_list.extend(quicksort(list_min))
    eq_num = len(list(filter(lambda x: x == first_elem, list_in)))
    for i in range(eq_num + 1):
        new_list.append(first_elem)
    list_max = list(filter(lambda x: x > first_elem, list_in))
    new_list.extend(quicksort(list_max))
    return new_list


if __name__ == "__main__":
    quicksort_test()
