from read import read_records
from confings import configure_argument


MODE_TO_FUNCTION = {
    'read_phone_book': read_records,
}


def main():
    arg_phone_book = configure_argument(MODE_TO_FUNCTION.keys())
    args = arg_phone_book.parse_args()

    phone_mode = args.mode
    MODE_TO_FUNCTION[phone_mode]()


if __name__ == '__main__':
    main()