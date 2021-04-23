def gcd(A, B):
    '''
    Возвращает наибольший общий делитель чисел A и B
    '''
    return A if not B else gcd(B, A % B)
