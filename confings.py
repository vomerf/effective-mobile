import argparse


def configure_argument(available_modes):
    parser = argparse.ArgumentParser(description='phonebook')
    parser.add_argument(
        'mode',
        choices=available_modes,
        help='Режимы работы телефонного справочника'
    )
    parser.add_argument('--record_id', type=str)
    parser.add_argument('--filename', help='имя файла телефонной книги')
    parser.add_argument(
        '--search-parametrs', nargs='+', help='параметры поиска'
    )
    return parser
