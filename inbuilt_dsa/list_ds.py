def create_list():
    return []

def add_element_to_list(lst, element):
    lst.append(element)
    return lst


def remove_element_from_list(lst, element):
    for ele in lst:
        if ele == element:
            lst.remove(ele)
            break
