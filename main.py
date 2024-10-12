import random


def main():
    total = 0
    numbers = []
    i = 0
    
    while total <= 100:
        scheisse = random.randint(0, 100)
        numbers[i] = 0
        while numbers[i] != scheisse:
            numbers[i] += 1
        print(numbers[i])
        scheisse = 0
        total += numbers[i]
        i += 1
        if total > 100:
            total - numbers
    print(total)

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
