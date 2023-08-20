from constants import BASE


def add_records():
    try:
        with open(BASE / 'phonebook.txt', 'a', encoding='utf-8') as f:
            name = input('Введите имя: ')
            last_name = input('Введите фамилию: ')
            middle_name = input('Введите отчество: ')
            name_organization = input('Введите название организации: ')
            work_phone = input('Введите рабочий телефон: ')
            personal_phone = input('Введите личный телефон: ')
            f.write(f"{name} {last_name} {middle_name} {name_organization} {work_phone} {personal_phone}\n")
    except FileNotFoundError:
        open('phonebook.txt', 'w').close()
