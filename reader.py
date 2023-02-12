from datetime import datetime

def printNotes(li: list):
    print('№| Дата| Заголовок| Заметка ')
    for i in li:
        print('| '.join(i))


def printAll(nameList: list):
    '''
    Печать списка отсортированного по дате
    :param nameList: Список
    :return:
    '''
    nameList.sort(key=lambda toPos: datetime.strptime(toPos[1], "%Y-%m-%d %H:%M:%S"), reverse=True)
    printNotes(nameList)


def nextID(nameList: list) -> str:
    '''
    Возвращает номер следующего ID
    :param nameList: Список заметок
    :return: ID следующей заметки
    '''
    m = 0
    for i in nameList:
        if int(i[0]) > m:
            m = int(i[0])
    return str(m + 1)


def newNote(nameList: list) -> list:
    '''
    Создание новой заметки и добавление её в список
    :param nameList: Список с заметками
    :return: Список с заметками и новой записью
    '''
    n = []
    head = str(input('Введите Заголовок: '))
    note = str(input('Введите Заметку: '))
    n.append(nextID(nameList))
    n.append(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
    n.append(head)
    n.append(note)
    if len(n) > 1:
        nameList.append(n)
    return nameList


def findNoteByDate(nameList: list) -> list:
    '''
    Найти заметки на определенную дату
    :param nameList: Список заметок
    :return: Список найденных заметок
    '''
    fData = str(input('Для вывода заметок за определенную дату введите дату в формате ГГГГММДД: '))
    try:
        dtNoteFind = datetime.strptime(fData, "%Y%m%d").date()
    except ValueError:
        print(f'Введен не корректный формат даты: "{fData}". Дату необходимо ввводить в формате ГГГГММДД.')
        return [1]

    li = []
    for line in nameList:
        dtNote = datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S").date()
        if dtNote == dtNoteFind:
            li.append(line)
    if len(li) == 0:
        print('За указанную дату заметок нет.')
        return [2]
    printNotes(li)
    return li

def editNoteByID(name_list: list, id: str) -> list:
    '''
    Редактируем список по ID
    :param name_list: Список
    :param id: id
    :return: Отредактированный список
    '''
    head = str(input('Введите Заголовок: '))
    note = str(input('Введите Заметку: '))
    for i in range(len(name_list)):
        if name_list[i][0] == str(id):
            name_list[i][1] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            name_list[i][2] = head
            name_list[i][3] = note
    return name_list


def checkID(nameList: list, id: str) -> int:
    '''
    Проверка наличия ID в списке
    :param nameList: Список
    :param id: ID
    :return: Успешная проверка 1, не успешная 0.
    '''
    ch = 0
    for i in range(len(nameList)):
        if nameList[i][0] == str(id):
            ch = 1
    return ch


def enterIdNoteForEdit(nameList: list) -> list:
    '''
    Запуск редактирования списка по ID
    :param nameList: Список для редактирования
    :return: Отредактированный список или не измененный список, если id не найден
    '''
    id = str(input('Введите номер заметки для редактирования: '))
    if checkID(nameList, id) == 1:
        editedList = editNoteByID(nameList, id)
        return editedList
    else:
        print('Нет такого номера заметки.')
        return nameList


def findNoteID(nameList: list, id: str) -> list:
    '''
    Функция ищет в списке списков список с 0-м членом равным id
    :param nameList: Список списков
    :param id: идентификатор в списке
    :return: Список с записью соответствующей искомому id
    '''
    try:
        int(id)
    except ValueError:
        print('ID не число.')
        return [1]
    li = []
    for i in range(len(nameList) - 1):
        if nameList[i][0] == str(id):
            li.append(nameList[i])

    if len(li) == 0:
        print(f'Заметок с ID: "{id}" нет.')
    else:
        printNotes(li)
    return li

def enterIdNoteForFind(nameList: list) -> list:
    id = str(input('Введите номер заметки для поиска: '))
    if checkID(nameList, id) == 1:
        editedList = findNoteID(nameList, id)
        return editedList
    else:
        print('Нет такого номера заметки.')
        return nameList



def deleteNoteByID(nameList: list, id: str) -> list:
    '''
    Удаление заметки по id если это возможно
    :param nameList: Список заметок
    :param id: id заметки
    :return: Обновленный список
    '''
    k = -1
    for i in range(len(nameList)):
        if nameList[i][0] == str(id):
            k = i
    if k != -1:
        del nameList[k]
        print(f'Запись с id {id} успешно удалена.')
    else:
        print(f'Запись с id {id} удалить не удалось.')
    return nameList


def enterIdNoteForDelete(nameList: list) -> list:
    '''
    Запуск удаления заметки по ID
    :param nameList: Список с заметкой для удаления
    :return: Результирующий список
    '''
    id = str(input('Введите номер заметки для удаления: '))
    if checkID(nameList, id) == 1:
        newList = deleteNoteByID(nameList, id)
        return newList
    else:
        print('Нет такого номера заметки.')
        return nameList