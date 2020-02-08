documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def name_list():
    try:
        for document in documents:
            if document.get('name') == '':
                raise KeyError
            print(document.get('name'))
    except KeyError:
        print(f'У документа не указан владелец!')


def find_person():
    document_number = input('Введите номер документа для поиска: ')
    for document in documents:
        if document_number == document['number']:
            return print('Документ {} принадлежит: {}.'.format(document_number, document['name']))
    return print('Такого документа нет.')


def enlist():
    for document in documents:
        print(document['type'], document['number'], document['name'])


def add():
    while True:
        doc_number = input('Введите номер документа: ')
        is_existing = 0
        for items in documents:
            if doc_number == items.get('number'):
                is_existing = 1
        if is_existing == 1:
            print('Такой документ уже есть!')
            continue
        else:
            break
    doc_type = input('Введите тип документа: ')
    doc_owner = input('Введите имя владельца документа: ')
    while True:
        doc_shelf = input('Введите номер полки, куда положить документ: ')
        shelf_list = []
        for items in directories.keys():
            shelf_list.append(items)
        if doc_shelf not in shelf_list:
            print('Такой полки нет')
            continue
        else:
            break
    new_doc = {'type': doc_type, 'number': doc_number, 'name': doc_owner}
    documents.append(new_doc)
    currently_on_shelf = directories.get(doc_shelf)
    currently_on_shelf.append(doc_number)
    new_doc_shelf = {doc_shelf: currently_on_shelf}
    directories.update(new_doc_shelf)
    print('Документ под номером {} успешно поставлен на полку {}'.format(doc_number, doc_shelf))


def new_shelf():
    while True:
        shelf_number = input('Введите номер новой полки: ')
        if str(shelf_number) in directories.keys():
            print('Такая полка уже существует.')
            continue
        elif int(shelf_number) <= 0:
            print('Неправильный номер полки. Введите значение больше нуля')
            continue
        else:
            break
    new_shelf_dict = {shelf_number: []}
    directories.update(new_shelf_dict)
    return print('Полка номер {} успешно создана'.format(shelf_number))


def shelf():
    document_number = input('Введите номер документа, а мы найдем его на полке: ')
    for keys, values in directories.items():
        for docs in values:
            if document_number == docs:
                return print('Документ найден на полке {}.'.format(keys))
    return print('На полках документ не найден')


def agenda():
    return print('\nДоступные команды:\np - найти человека по номеру документа\nl - список всех документов\nll - '
                 'список всех владельцев документов\ns - поиск '
                 'документа на полке\nd - удалить документ\na - добавить новый документ\nas - создать новую полку\nm - '
                 'переместить документ с полки на полку\nq - выход')


def delete():
    doc_number = input('Какой документ нужно удалить? ')
    doc_position = 1
    doc_shelf = 0
    for items in documents:
        if doc_number == items.get('number'):
            break
        else:
            doc_position += 1
    if doc_position > len(documents):
        print('Документа с таким номером нет.')
        return
    for keys, values in directories.items():
        for items in values:
            if doc_number == items:
                doc_shelf = keys
    dictionary_to_delete = documents[doc_position - 1]
    documents.remove(dictionary_to_delete)
    shelf_info = directories.get(doc_shelf)
    shelf_info.remove(doc_number)
    updated_shelf_info = {doc_shelf: shelf_info}
    directories.update(updated_shelf_info)
    print('Документ {} успешно удален с полки {}.'.format(doc_number, doc_shelf))


def move():
    doc_number = input('Какой документ нужно переместить? ')
    doc_position = 1
    current_shelf = 0
    for items in documents:
        if doc_number == items.get('number'):
            break
        else:
            doc_position += 1
    if doc_position > len(documents):
        print('Документа с таким номером нет.')
        return
    for keys, values in directories.items():
        for items in values:
            if doc_number == items:
                current_shelf = keys
    target_shelf = input('На какую полку перенести документ? ')
    if target_shelf not in directories.keys():
        print('Такая полка не существует.')
        return
    if target_shelf == current_shelf:
        print('Документ уже находится на этой полке.')
        return
    shelf_info = directories.get(current_shelf)
    shelf_info.remove(doc_number)
    updated_shelf_info = {current_shelf: shelf_info}
    directories.update(updated_shelf_info)
    target_shelf_info = directories.get(target_shelf)
    target_shelf_info.append(doc_number)
    updated_shelf_info = {target_shelf: target_shelf_info}
    directories.update(updated_shelf_info)
    print('Документ {} успешно перенесен с полки {} на полку {}.'.format(doc_number, current_shelf, target_shelf))


def main():
    while True:
        print()
        print('*' * 20, 'Архив', '*' * 20)
        todo = input('Введите команду (h для помощи):\n> ')
        if todo == 'q':
            break
        elif todo == 'h':
            agenda()
        elif todo == 'p':
            find_person()
        elif todo == 'l':
            enlist()
        elif todo =='ll':
            name_list()
        elif todo == 's':
            shelf()
        elif todo == 'a':
            add()
        elif todo == 'd':
            delete()
        elif todo == 'as':
            new_shelf()
        elif todo == 'm':
            move()
        else:
            print('Несуществующая команда. Используйте h для помощи.')


main()
