from valid import valid_az

# This function alphabetically sorts the list


def sort_list(list_to_sort):  # Nicole's Module
    sorting_method = valid_az("Press 'A' to sort from A-Z or 'Z' to sort from Z-A: ")
    if sorting_method == "a":
        return list_to_sort.sort()
    else:
        return list_to_sort.sort(reverse=True)