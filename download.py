import requests
import urllib
import shutil
import os.path

r = requests.get('http://music.163.com/api/playlist/detail?id=335280')

arr = r.json()['result']['tracks']

music_number = len(arr)

for i in range(music_number):
    name = arr[i]['name'] + '.mp3'
    files = os.path.isfile('/home/d/Music/' + name)
    if not files:
        link = arr[i]['mp3Url']
        urllib.urlretrieve(link, name)
        shutil.move('/home/d/github/cloudmusic/' + name, '/home/d/Music')
        print name + ' Download Complete.'
    else:
        print name + ' Exist!'

print 'All Files Download Complete!'
