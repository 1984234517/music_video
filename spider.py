import requests
import re
import os
import hashlib

base_dir = '歌曲/'
if not os.path.exists(base_dir):
    os.mkdir(base_dir)
class Baidu_song_api(object):
    def __init__(self):
        self.song_id = ''
        self.headers = {
            'Referer': 'http://music.taihe.com/search?key=%E6%BC%94%E5%91%98',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
    def md5_encry(self, data):
        return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    def get_song_id(self,key):
        secret = "0b50b02fd0d73a9c4c8c3a781c30845f"
        r = "appid=16073360&timestamp=1647579672&type=&word={}".format(key)
        data = r+secret
        sign = self.md5_encry(data)
        print('39d7f2b73b3807712eb241b78c0db5a6')
        print(sign)
        url = 'https://music.91q.com/v1/search?sign={}&word={}&type=1&pageSize=20&appid=16073360&timestamp=1647579672'.format(sign, key)
        html = requests.get(url, headers= self.headers)
        html.encoding = 'utf-8'
        res=html.json()
        print(res)
        for i in res['data']['typeTrack']:
            self.song_id.append(i['TSID'])

    def get_song_information(self):
        for song_id in self.song_id:
            url = 'http://music.91q.com/v1/song/tracklink?sign=615cc279596a7ec10c6e46edcc8f3ca6&appid=16073360&TSID={}&timestamp=1647578839'.format(song_id)
            html = requests.get(url, headers=self.headers).json()
            print(html['data']['path'])
    def save_song(self):
        song_information = self.html['data']['songList']

        for i in range(len(song_information)):
            if i==10:
                break
            dirname = base_dir + song_information[i]['artistName'] + '\\'
            if not os.path.exists(dirname):
                os.mkdir(dirname)
            filename = dirname+song_information[i]['songName']+song_information[i]['artistName']+'.'+song_information[i]['format']
            lrc_filename = dirname+song_information[i]['songName']+song_information[i]['artistName']
            lrc_url = song_information[i]['lrcLink']

            song_url = song_information[i]['songLink']
            print('歌名：', filename, '歌词地址：', lrc_url, '歌曲下载地址：', song_url)
            # 下载歌曲F:\python\python_code\cramler_code\百度音乐\歌曲
            # song = requests.get(song_url, headers=self.headers).content
            # with open(str(filename), 'wb')as fp:
            #     fp.write(song)
            # print("歌曲下载好了")
            # # 下载歌词
            # if lrc_url:
            #     song_lrc = requests.get(lrc_url).text
            #     with open(lrc_filename+'.txt', 'w') as fp:
            #         fp.write(song_lrc)
            # else:
            #     print("该歌曲没有找到歌词")
    def main(self,value):
        kk = Baidu_song_api()
        kk.get_song_id(value)
        kk.get_song_information()
        # kk.save_song()

if __name__ == "__main__":
    kk = Baidu_song_api()
    key = input('请输入你想要爬取的歌手或者歌名')
    kk.main(key)