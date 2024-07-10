from valid import valid_az


def sort_list(list_to_sort):
    sorting_method = valid_az("Press 'A' to sort from A-Z or 'Z' to sort from Z-A: ")
    if sorting_method == "a":
        return list_to_sort.sort()
    else:
        return list_to_sort.sort(reverse=True)