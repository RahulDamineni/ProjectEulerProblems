# coding=utf-8


def palindrome_check(number):
    """ Checks if a number is palindrome """
    number = str(number)
    if len(number) < 6:
        return False
    return number == number[::-1]

def generate_possibilities():
    """ Generates all possibilites quickly for reuse """
    possibilities = []
    a = 100
    while a < 1000:
        b = 100
        while b < 1000:
            if palindrome_check(a*b):
                possibilities.append(a*b)
            b += 1
        a += 1
    return sorted(possibilities, reverse=True)

if __name__ == '__main__':

    possibilites = generate_possibilities()
    input_num = 101110
    for num in possibilites:
        if num < input_num:
            print num
            break




