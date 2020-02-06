import math

def prime_factors(n):
    prime_list = []
    while n % 2 == 0:
        prime_list.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            prime_list.append(i)
            n = n / i

    if n > 2:
        prime_list.append(n)

    return prime_list

def sum_cubs(prime_list):
    total = 0
    for n in prime_list:
        total += n**3
    return total

if __name__ == '__main__':
    input_list = [3, 9, 4, 10, 987654321]

    for input in input_list:
        prime_list = prime_factors(input)
        total = sum_cubs(prime_list)
        print(input, total)
