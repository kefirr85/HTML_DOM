def test(*params):
    print(params)
    print('Kefirr:', 39,'age')
test()
test(1,2,3)
test('Kef: ', 39)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))