def collatz(num):
    if num % 2 == 0:
        print(f'\n\nthe number is even :\n  {num} // 2')
    else:
        print(f'\n\nthe number is odd:\n 3 * {num} + 1')
    return (num / 2) if num % 2 == 0 else (3 * num + 1)

while True:
    try:
        number=int(input('\ntype in a number : '))
        ans = collatz(number)
        print(f'= {ans}')
    except ValueError as e:
        print("<ERROR>- [ Input should be an integer ]\n\n")