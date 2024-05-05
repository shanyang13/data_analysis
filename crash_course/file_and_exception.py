from pathlib import Path
import json


def divide_number():
    while True:
        first_number = input('Enter first number: ')
        if first_number == 'q':
            break
        second_number = input('Enter second number: ')
        if second_number == 'q':
            break
        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print('shit')
        else:
            print(answer)


if __name__ == '__main__':
    path = Path('pi_digits.txt')
    contents = path.read_text().rstrip()
    print(contents)
    print('-------------')

    line = contents.splitlines()
    print(line)
    for line in line:
        print(line)
    print('-------------')

    lines = contents.splitlines()
    pi_string = ''
    for line in lines:
        print(line)
        pi_string += line.strip()
    print(pi_string)
    print(len(pi_string))

    contents2 = 'I love pi!\n'
    contents2 += 'I love p2\n'
    contents2 += 'I love p3'

    path2 = Path('programming.txt')
    path2.write_text(contents2)
    print('---------------')

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    path3 = Path('numbers.json')
    contents3 = json.dumps(numbers)
    path3.write_text(contents3)
    print('写json文件')
    print('---------------')

    path4 = Path('numbers.json')
    contents4 = path4.read_text()
    numbers2 = json.loads(contents4)
    print(numbers2)