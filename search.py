from constants import BASE


def search_phonebook(filename='phonebook.txt', *args):
    '''Поиск производится по всем полям:
    - lastname
    - name
    - middlename
    - name_organization
    - work_phone
    - personal_phone
    Поиск производится от первого до последнего параметра
    сначала lastname, затем name и так далее ниже по списку.
    Совпадение должно быть полным, для того чтобы произвести поиск нужно
    передать два необязательных параметра в консоль
    это --filename и --search-parametrs.
    В параметр filename передаем параметр текстового документа
    в котором хотим произвести поиск
    например phonebook.txt. Когда производим поиск в параметр
    search-parametrs передаем через пробел
    поля по которым хотим проихвести поиск например если хотим
    произвести поиск по фамилии то
    передать можно только один параметр --search-paametrs Иванов,
    просто по имени не получится
    произвести поиск только по порядку, если хотим сделать поиск по
    имени то надо передать первым параметром
    фамили и только затем имя и так со всеми параметрами в их порядке
    который представлен выше, напрмер
    --search-parametrs Иванов Иван Иванович Билайн 89998927126 89998927126.
    Данные выводятся в консоль в виде списков.
    '''
    with open(BASE / filename, 'r', encoding='utf-8') as file:
        for line in file:
            record = line.strip().split(' ')
            if all(record[i + 1] == value for i, value in enumerate(args)):
                yield record


def search_records(search_parametr):
    for record in search_phonebook(
        search_parametr.filename, *search_parametr.search_parametrs
    ):
        print(record)
