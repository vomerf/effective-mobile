import re
import uuid

from constants import BASE


def add_records() -> None:
    '''Добавляет запись в отсортированном порядке'''
    try:
        with open(BASE / 'phonebook.txt', 'r', encoding='utf-8') as f:
            records = [line.strip() for line in f.readlines()]
        records.append(create_new_record())
        records.sort()
        with open(BASE / 'phonebook.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(records) + '\n')
    except FileNotFoundError:
        with open(BASE / 'phonebook.txt', 'w', encoding='utf-8'):
            pass


def correct_name(title: str, text: str) -> str:
    while not re.match(r'^[А-Я][а-я]*$', title):
        title: str = input(text)
    return title


def create_new_record() -> str:
    record_id = str(uuid.uuid4())[:8]
    last_name = input('Введите фамилию: ')
    correct_name(
        last_name,
        'Введите корректно фамилию'
        '(Должно начинаться с большой буквы и на кириллице): '
    )
    name = input('Введите имя: ')
    correct_name(
        name,
        'Введите корректно имя'
        '(Должно начинаться с большой буквы и на кириллице): '
    )
    middle_name = input('Введите отчество: ')
    correct_name(
        middle_name,
        'Введите корректно отчество'
        '(Должно начинаться с большой буквы и на кириллице): '
    )
    name_organization = input('Введите название организации: ')
    work_phone = input('Введите рабочий телефон: ')
    personal_phone = input('Введите личный телефон: ')

    return (
        f'{record_id} '
        f'{last_name} {name} '
        f'{middle_name} {name_organization} '
        f'{work_phone} {personal_phone}'
    )
