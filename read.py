from constants import BASE


def read_records() -> None:
    '''Читает постранично записи,
    если файла не существует он создает пустой файл
    с названием по умолчанию phonebook.txt
    '''
    try:
        with open(
            BASE / 'phonebook.txt', 'r', encoding='utf-8'
        ) as f:
            page_size: int = 5
            page_num: int = 1
            lines: list = f.readlines()
            while True:
                start: int = (page_num - 1) * page_size
                end: int = start + page_size
                page_lines: list = lines[start:end]
                if not page_lines:
                    break
                print('Страница', page_num)
                print(''.join(page_lines))
                input('Нажмите Enter для продолжения...')
                page_num += 1

    except FileNotFoundError:
        open('phonebook.txt', 'w').close()
