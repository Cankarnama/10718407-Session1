import random

def sum_multiply(array):              # We pass a parameter (upperLimit) when declaring the function
    summ = 0
    multiply = 1
    for number in array:
        summ += number
        multiply *= number
    return summ, multiply


while True:
    try:
        lower=int(input('\ntype in the lower limit: '))
        upper=int(input('type in the upper limit: '))
        array = []
        for i in range(10):
            array.append(random.randrange(lower, upper))
        print(array)
        sum_total, multiply_total = sum_multiply(array)
        print(f'sum of the array is {sum_total}\nproduct of the array is {multiply_total}')
    except ValueError as e:
        print("<ERROR>- [ Input should be an integer ]\n\n")
