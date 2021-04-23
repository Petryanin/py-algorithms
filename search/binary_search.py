def binary_search(needle, haystack):
    '''
    Возвращает True, если элемент needle есть 
    в упорядоченной последовательности haystack.
    В противном случае False.
    '''
    middle = len(haystack) // 2
    if len(haystack) == 1 and needle != haystack[middle]:
        return False
    if needle == haystack[middle]:
        return True
    if needle < haystack[middle]:
        return binary_search(needle, haystack[:middle])
    else:
        return binary_search(needle, haystack[middle:])
