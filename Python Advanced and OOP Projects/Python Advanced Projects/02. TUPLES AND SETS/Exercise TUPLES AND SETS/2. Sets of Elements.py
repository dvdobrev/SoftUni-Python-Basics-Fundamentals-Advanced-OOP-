n, m = [int(el) for el in input().split()]

n_set = set()
m_set = set()

for el in range(n):
    num = int(input())
    n_set.add(num)

for el in range(m):
    num = int(input())
    m_set.add(num)

definied = n_set.intersection(m_set)

for el in definied:
    print(el)