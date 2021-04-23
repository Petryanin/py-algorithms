def linear_search(needle, haystack):
    '''
    Возвращает индекс первого вхождения итерируемого объекта needle 
    в итерируемый объект haystack.
    Если вхождение не найдено, возвращает -1
    '''
    for i in range(len(haystack)):
        result = i
        for j in range(len(needle)):
            if i < len(haystack) and needle[j] == haystack[i]:
                i += 1
            else:
                result = -1
                break
        else:
            return result
    return result
