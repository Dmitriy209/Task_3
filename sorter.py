import os
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
#Создание списка всех файлов в папке
arr = os.listdir('D:\погромирование\Task_3\Подборка музыки')
print(arr)

mp3 = MP3File('D:\погромирование\Task_3\Подборка музыки\A Day To Remember - Since U Been Gone.mp3')

tags = mp3.get_tags()
print(tags)
"""
Output:
{'ID3TagV1': {'song': 'Prowler', 'artist': 'Iron Maiden', 'album': 'Iron Maiden',
'year': '1980', 'comment': None, 'track': 1, 'genre': 'Other'},
'ID3TagV2': {'artist': 'Iron Maiden', 'band': 'Iron Maiden', 'album': 'Iron Maiden',
'song': 'Prowler', 'track': '1/9', 'genre': 'Heavy Metal', 'year': '1980'}}
"""
#Извлечение музыки
ID3TagV1=tags['ID3TagV1']
song=ID3TagV1['song']
artist=ID3TagV1['artist']
album=ID3TagV1['album']
print('song ', song)
print('artist ', artist)
print('album ', album)
#Извлечение тегов в словарь
dict={}
dict1={song:1}
print(dict)
dict.update({song:{artist:album}})
print(dict)
