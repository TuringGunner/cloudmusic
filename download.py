import requests
import urllib
import shutil

r = requests.get('http://music.163.com/api/playlist/detail?id=335280')

arr = r.json()['result']['tracks']

music_number = len(arr)

for i in range(music_number):
    name = arr[i]['name'] + '.mp3'
    link = arr[i]['mp3Url']
    urllib.urlretrieve(link, name)
    shutil.move('/home/d/github/cloudmusic/' + name, '/home/d/Music')
    print name + ' Download Complete.'

print 'All Files Download Complete!'
