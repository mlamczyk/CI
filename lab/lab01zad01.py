import math

def prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2

    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True


def select_primes(list):
    p_list = []
    for i in list:
        if prime(i):
            p_list.append(i)
    return p_list


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 17]
print(select_primes(lista))
print(prime(9))
