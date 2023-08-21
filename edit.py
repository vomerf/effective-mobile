from constants import BASE


def edit_records(record_id: str):
    '''
    Для редоктирования записи нужно указать его уникальный
    идентификатор record_id этот параметр нужно передавать
    при запуске кода --record_id
    например `py main.py edit_in_phone_book --record_id 123`.
    Будет редактироваться запись под индексом 123.
    Если такого индекса не существует он вам скажет,
    что такой записи не существует.
    '''
    with open(BASE / 'phonebook.txt', 'r', encoding='utf-8') as f:
        lines: list = f.readlines()
    for index, line in enumerate(lines):
        if line.startswith(record_id):
            fields: list = line.split()[1:]
            last_name: str = fields[0]
            name: str = fields[1]
            middle_name: str = fields[2]
            name_organization: str = fields[3]
            work_phone: str = fields[4]
            personal_phone: str = fields[5]
            new_last_name: str = input(
                f'Текущая фамилия: {last_name}.'
                f'Введите новую фамилию или нажмите Enter,'
                f'чтобы оставить текущее значение: '
            )
            new_name: str = input(
                f'Текущее имя: {name}.'
                f'Введите новое имя или нажмите Enter,'
                f'чтобы оставить текущее значение: '
            )
            new_middle_name: str = input(
                f'Текущее отчество: {middle_name}.'
                f'Введите новое отчество или нажмите Enter,'
                f'чтобы оставить текущее значение: '
            )
            new_name_organization: str = input(
                f'Текущая организация: {name_organization}.'
                f'Введите новую организацию или нажмите Enter,'
                f'чтобы оставить текущее значение: '
            )
            new_work_phone: str = input(
                f'Текущий рабочий телефон: {work_phone}.'
                f'Введите новый рабочий телефон или нажмите Enter,'
                f'чтобы оставить текущее значение: '
            )
            new_personal_phone: str = input(
                f'Текущий личный телефон: {personal_phone}.'
                f'Введите новый личный телефон или нажмите Enter,'
                f'чтобы оставить текущее значение: '
            )

            new_line: str = (
                f'{record_id} {new_last_name if new_last_name else last_name} '
                f'{new_name if new_name else name} '
                f'{new_middle_name if new_middle_name else middle_name} '
                f'{new_name_organization if new_name_organization else name_organization} '
                f'{new_work_phone if new_work_phone else work_phone} '
                f'{new_personal_phone if new_personal_phone else personal_phone}\n'
                )
            lines[index] = new_line
            break
    else:
        print(f'Запись с идентификатором {record_id} не найдена')
        return
    with open(BASE / 'phonebook.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f'Запись с идентификатором {record_id} успешно отредактирована')
