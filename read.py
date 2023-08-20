from constants import BASE


def read_records():
    try:
        with open(
            BASE / 'phonebook.txt', 'r', encoding='utf-8'
        ) as f:
            page_size = 5
            page_num = 1
            lines = f.readlines()
            while True:
                start = (page_num - 1) * page_size
                end = start + page_size
                page_lines = lines[start:end]
                if not page_lines:
                    break
                print('Страница', page_num)
                print(''.join(page_lines))
                input('Нажмите Enter для продолжения...')
                page_num += 1

    except FileNotFoundError:
        open('phonebook.txt', 'w').close()
