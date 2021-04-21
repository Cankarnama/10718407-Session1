import random
while True:
    try:
        lower=int(input('\ntype in the lower limit: '))
        upper=int(input('type in the upper limit: '))
        array = []
        for i in range(10):
            array.append(random.randrange(lower, upper))
        print(array)
    except ValueError as e:
        print("<ERROR>- [ Input should be an integer ]\n\n")

