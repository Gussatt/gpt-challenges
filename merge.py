def merge_lists(list_a, list_b):
    merged_list = []
    i = 0
    j = 0

    len_a = len(list_a)
    len_b = len(list_b)

    while i < len_a and j < len_b:
        if list_a[i] < list_b[j]:
            merged_list.append(list_a[i])
            i += 1
        else:
            merged_list.append(list_b[j])
            j += 1

    while i < len_a:
        merged_list.append(list_a[i])
        i += 1

    while j < len_b:
        merged_list.append(list_b[j])
        j += 1

    return merged_list


list_a = [2, 5, 8]
list_b = [3, 6, 9, 10]
print(merge_lists(list_a, list_b))
