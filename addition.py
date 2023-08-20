import re
from constants import BASE


def add_records():
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


def correct_name(title, text):
    while not re.match(r'^[А-Я][а-я]*$', title):
        title = input(text)
    return title

### Доделать регулярное выражение для мобильного телефона ###
# def correct_mobile_phone(title, text):
#     while not re.match(r'^(?:\+7|8)\d{10}$', title):
#         phone = input(text)
#     return phone


def create_new_record():
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
        f'{last_name} {name} '
        f'{middle_name} {name_organization} '
        f'{work_phone} {personal_phone}'
    )

add_records()

# def add_records():
#     try:
#         with open(BASE / 'phonebook.txt', 'a', encoding='utf-8') as f:
#             name = input('Введите имя: ')
#             last_name = input('Введите фамилию: ')
#             middle_name = input('Введите отчество: ')
#             name_organization = input('Введите название организации: ')
#             work_phone = input('Введите рабочий телефон: ')
#             personal_phone = input('Введите личный телефон: ')
#             f.write(
#                 f'{name} {last_name}'
#                 f'{middle_name} {name_organization}'
#                 f'{work_phone} {personal_phone}\n'
#             )
#     except FileNotFoundError:
#         open('phonebook.txt', 'w').close()
