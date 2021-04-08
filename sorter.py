import os
import glob
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

# Создание списка всех файлов в папке
arr = os.listdir('D:\погромирование\Task_3\Подборка музыки')
print(arr)
# Цикл для переборки файлов в директории
namedir = input("Введите директорию: ")

# Цикл создает директорию с именем исполнителя для каждого файла в указанной директории
for j in range(len(arr)):
    os.chdir(namedir)  # Перемещение в нужную директорию
    file = os.path.abspath(arr[j])  # Извлечение абсолютного пути из файла
    print(file)
    mp3 = MP3File(file) # Извлечение тегов
    tags = mp3.get_tags()
    ID3TagV1 = tags['ID3TagV1']
    song = ID3TagV1['song']
    artist = ID3TagV1['artist']
    album = ID3TagV1['album']
    print('Цикл if', song, artist, album)
    # Цикл для значений None
    if song is None or artist is None or album is None:
        if song is None:
            # print('SOOOOOOOOOOOOONG')
            song=arr[j]
            song=song[:-4]  # Удаление последних 4х символов .mp3
        if artist is None:
            # print('ARTIIIIIIIIIIIIIST')
            artist = arr[j]
            artist = artist[:-4]  # Удаление последних 4х символов .mp3
        if album is None:
            # print('ALBUUUUUUUUUUUM')
            album = arr[j]
            album = album[:-4]  # Удаление последних 4х символов .mp3
    # print('Цикл if прошел\n','song ',song,'\n', 'artist ', artist, '\n','album', album)
    # print('song ', song)
    # print(ID3TagV1)
    # print('artist ', artist)
    # print('album ', album)
    # print(arr[j])
    os.mkdir(artist)  # Создание директории
    j+=1