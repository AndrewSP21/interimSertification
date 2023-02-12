def readNote(nameFile: str) -> list:
    '''
    Чтение файла в список
    :param nameFile: Имя файла
    :return: Список
    '''
    li = []
    try:
        with open(nameFile, "r", encoding='utf-8-sig') as f_obj:

            ct = 0
            for line in f_obj:
                ct += 1
                content = line.replace("\n", "").split(';')
                try:
                    int(content[0])
                except ValueError:
                    print(f'Ошибка чтения файла заметок. В строке {ct}: Не корректное ID заметки "{content[0]}".')
                    return [2]
                li.append(content)
        return li
    except FileNotFoundError:
        return li
    except OSError:
        print('Ошибка чтения файла, будет создан новый файл')
        return li
    except EOFError:
        print('Ошибка чтения файла, будет создан новый файл')
        return li



def saveNotes(nameList: list, nameFile: str):
    '''
    Сохранение списка в файл
    :param nameList: Список для записи в файл
    :param nameFile: имя файла
    :return:
    '''
    try:
        with open(nameFile, "w", encoding='utf-8-sig') as f_obj1:
            for i in nameList:
                f_obj1.write(';'.join(i) + '\n')

            print('Заметки успешно сохранены.')
    except PermissionError:
        print('Ошибка. Недостаточно прав для создания файла')
    except OSError as e:
        print(f'Ошибка при сохранении файла: {e}')
