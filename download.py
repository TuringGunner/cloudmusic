import requests
import urllib

r = requests.get('http://music.163.com/api/playlist/detail?id=335280')

arr = r.json()['result']['tracks']

music_number = len(arr)

for i in range(music_number):
    name = arr[i]['name'] + '.mp3'
    link = arr[i]['mp3Url']
    urllib.urlretrieve(link, name)
    print name + ' download complete.'

print 'all files download complete!'
