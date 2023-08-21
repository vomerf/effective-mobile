from confings import configure_argument
from constants import MODE_TO_FUNCTION


def main():
    arg_phone_book = configure_argument(MODE_TO_FUNCTION.keys())
    args = arg_phone_book.parse_args()

    phone_mode = args.mode
    if phone_mode == 'edit_in_phone_book':
        MODE_TO_FUNCTION[phone_mode](args.record_id)
    elif phone_mode == 'search_in_phone_book':
        MODE_TO_FUNCTION[phone_mode](args)
    else:
        MODE_TO_FUNCTION[phone_mode]()
    

if __name__ == '__main__':
    main()
