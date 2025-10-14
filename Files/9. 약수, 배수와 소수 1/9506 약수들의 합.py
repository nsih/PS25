import sys

while True:
    n = int(sys.stdin.readline())

    if n == -1:
        break

    divisors = []

    if n > 1:
        divisors.append(1)

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)

    if sum(divisors) == n:
        print(f"{n} = {' + '.join(map(str, sorted(divisors)))}")
    else:
        print(f"{n} is NOT perfect.")