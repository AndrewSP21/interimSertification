from reader import printAll, newNote, findNoteByDate, enterIdNoteForFind, enterIdNoteForEdit, enterIdNoteForDelete
from workWithFiles import saveNotes


def menu() -> int:
    m = """
    Управление заметками:

    1. Вывести все заметки
    2. Добавить новую заметку
    3. Вывести заметки на дату
    4. Найти заметку по ID
    5. Редактировать заметку по ID
    6. Удалить заметку по ID
    7. Сохранить изменения
    8. Выйти
    """
    try:
        choiceMenu = int(str(input(m)))
    except ValueError:
        print('Программа завершена. Введено не число.')
        return -1

    if choiceMenu in range(1, 9):
        return choiceMenu
    else:
        print(f'Программа завершена.')
        return -2





def control(nS: list, nameFile: str):
    mn = -3

    while mn != -2:
        mn = menu()

        if mn == 1:
            printAll(nS)
        elif mn == 2:
            nS = newNote(nS)
        elif mn == 3:
            dn = findNoteByDate(nS)
        elif mn == 4:
            fni = enterIdNoteForFind(nS)
        elif mn == 5:
            nS = enterIdNoteForEdit(nS)
        elif mn == 6:
            nS = enterIdNoteForDelete(nS)
        elif mn == 7:
            saveNotes(nS, nameFile)
        else:
            exit(0)
