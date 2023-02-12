from controller import control

from workWithFiles import readNote, saveNotes


if __name__ == '__main__':
    nameFile = 'notes.csv'
    nS = readNote(nameFile)
    control(nS, nameFile)











