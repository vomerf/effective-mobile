import argparse


def configure_argument(available_modes):
    parser = argparse.ArgumentParser(description='phonebook')
    parser.add_argument(
        'mode',
        choices=available_modes,
        help='Режимы работы телефонного справочника'
    )
    return parser
