def brackets(sequence):
    '''
    Возвращает True, если переданная последовательность скобок правильная.
    Иначе False.
    '''
    open_brackets = ('(', '[', '{')
    close_brackets = (')', ']', '}')
    stack = []

    for bracket in sequence:
        if bracket in open_brackets:
            stack.append(bracket)
        elif not stack:
            return False
        elif close_brackets.index(bracket) != open_brackets.index(stack.pop()):
            return False

    return True if not stack else False
