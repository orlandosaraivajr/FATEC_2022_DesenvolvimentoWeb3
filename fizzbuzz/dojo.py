def fizzbuzz(numero):
    if numero % 15 == 0:
        return 'fizzbuzz'
    elif numero % 5 == 0:
        return 'buzz'
    elif numero % 3 == 0:
        return 'fizz'
    return numero


for number in list(range(1, 101)):
    print(fizzbuzz(number))

assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(3) == 'fizz'
assert fizzbuzz(5) == 'buzz'
assert fizzbuzz(6) == 'fizz'
assert fizzbuzz(7) == 7
assert fizzbuzz(10) == 'buzz'
assert fizzbuzz(15) == 'fizzbuzz'
assert fizzbuzz(16) == 16
assert fizzbuzz(17) == 17
assert fizzbuzz(30) == 'fizzbuzz'
