import os
import glob
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

#Создание списка всех файлов в папке
arr = os.listdir('D:\погромирование\Task_3\Подборка музыки')
print(arr)
#Цикл для переборки файлов в директории
namedir=input("Введите директорию: ")
os.chdir(namedir) #Перемещение в нужную директорию
#Цикл создает директорию с именем исполнителя для каждого файла в указанной директории
for j in range(len(arr)):
    # Извлечение тегов
    file = os.path.abspath(arr[j])
    print(file)
    mp3 = MP3File(file)
    tags = mp3.get_tags()
    ID3TagV1 = tags['ID3TagV1']
    song = ID3TagV1['song']
    artist = ID3TagV1['artist']
    album = ID3TagV1['album']
    #print('song ', song)
    #print('artist ', artist)
    #print('album ', album)
    print(arr[j])
    os.mkdir(artist) #Создание директории
    j+=1


#print(tags)

#Извлечение тегов в словарь
#dict={}
#dict1={song:1}
#print(dict)
#dict.update({song:{artist:album}})
#print(dict)
#print('os.walk')

#попытка создания цикла для взятие имен файлов
#for i in os.walk('D:\погромирование\Task_3\Подборка музыки'):
#    print('Начало')
#    print(i[2])
#    print('Конец')