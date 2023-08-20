import argparse


def configure_argument(available_modes):
    parser = argparse.ArgumentParser(description='phonebook')
    parser.add_argument(
        'mode',
        choices=available_modes,
        help='Режимы работы телефонного справочника'
    )

    parser.add_argument(
        '-r',
        '--read_records',
        action='store_true',
        help='Чтение всех страниц телефонной книги'
    )

    parser.add_argument(
        '-a',
        '--add-record',
        action='store_true',
        help='Добавление записи в телефонную книгу'
    )
    return parser
