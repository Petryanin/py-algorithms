from collections import namedtuple


def atm(bill: list, value: int):
    '''
    Возвращает кортеж, первый элемент - минимальное количество купюр, требуемых
    для составления суммы запроса; второй - список купюр
    '''
    inf = value + 10
    f = [inf] * inf
    f[0] = 0
    prev = [-1] * inf
    for i in range(1, value + 1):
        for j in range(len(bill)):
            if i - bill[j] >= 0 and f[i - bill[j]] < f[i]:
                f[i] = f[i - bill[j]]
                prev[i] = bill[j]
        f[i] += 1
    return (f[value], prev)


bills = [1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000, 5000]
value = 18750

ATM = namedtuple('ATM', 'bill_quantity bill_list')

ans = ATM(*atm(bills, value))
print(ans.bill_quantity)

curr = value
bill = []
while curr:
    bill.append(ans.bill_list[curr])
    curr -= ans.bill_list[curr]

print(*bill)
