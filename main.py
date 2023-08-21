import argparse
from confings import configure_argument
from addition import add_records
from edit import edit_records
from read import read_records
from search import search_records


MODE_TO_FUNCTION: dict = {
    'read_phone_book': read_records,
    'add_in_phone_book': add_records,
    'edit_in_phone_book': edit_records,
    'search_in_phone_book': search_records
}


def main() -> None:
    arg_phone_book: argparse.ArgumentParser = (
        configure_argument(MODE_TO_FUNCTION.keys())
    )
    args = arg_phone_book.parse_args()

    phone_mode: str = args.mode
    if phone_mode == 'edit_in_phone_book':
        MODE_TO_FUNCTION[phone_mode](args.record_id)
    elif phone_mode == 'search_in_phone_book':
        MODE_TO_FUNCTION[phone_mode](args)
    else:
        MODE_TO_FUNCTION[phone_mode]()


if __name__ == '__main__':
    main()
