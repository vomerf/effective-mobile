import argparse
from constants import BASE


def search_phonebook(filename='phonebook.txt', *args):
    '''Поиск производится по всем полям:
    '''
    with open(BASE / filename, 'r', encoding='utf-8') as file:
        for line in file:
            record = line.strip().split(' ')
            if all(record[i + 1] == value for i, value in enumerate(args)):
                yield record


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search phonebook')
    parser.add_argument('filename', help='name of the phonebook file')
    parser.add_argument('args', nargs='+', help='search parameters')
    search_parametr = parser.parse_args()


for record in search_phonebook(search_parametr.filename, *search_parametr.args):
    print(record)