import json, requests
from Crypto.Cipher import AES
import base64
import time

'''
@author: tan
该文件中的音乐接口来自于下歌吧音乐下载平台
网址为：https://music.y444.cn/#/
'''


class myAES(object):
    def __init__(self):
        # CBC模式下，数据长度需要是16字节的整数倍
        self.BLOCK_SIZE = 16
        # 偏移量
        self.iv = '0102030405060708'
        # 　解密密钥
        self.decryptKey = '2wVGQU6CMFpZzMQX'
        # 注意这里的加密key和sec_key是对应的
        self.encryptKey = 'HHij7Xc6dkDe6izN'
        self.sec_key = "cVstaEdlc/VXLXjusGz88EwjJlkZMC0UMSi2KIZNTgPZhHaPNEMn+KttW9A83NXCOiyeGwXB10KghIk4NG8XsEZpLvjoqhuKmdUjAye4Xf/F3ySEPTBdJ1RBgGCBy4jA6me81GTRcsF88Zd7Ei5NjUUb2hqyAbZY4eqCqohiE5w="

    # 填充，使得数据对齐16字节
    def pad(self, text):
        return text + (self.BLOCK_SIZE - len(text) % self.BLOCK_SIZE) * chr(self.BLOCK_SIZE - len(text) % self.BLOCK_SIZE)

    # 去掉填充，还原数据
    def unpad(self, text):
        return text[:-ord(text[len(text) - 1:])]

    def decrypt(self, text):
        aes = AES.new(self.decryptKey.encode('UTF-8'), AES.MODE_CBC, self.iv.encode('UTF-8'))
        text = base64.decodebytes(text.encode('UTF-8'))
        den_text = aes.decrypt(text)
        den_text = self.unpad(den_text)
        return den_text.decode("UTF-8")

    def encrypt(self, text):
        text = self.pad(json.dumps(text))
        # text = pad(text)
        encryptor = AES.new(self.encryptKey.encode(), AES.MODE_CBC, self.iv.encode())
        result = encryptor.encrypt(text.encode("UTF8"))
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        rdd = base64.b64encode(result).decode("UTF8")
        return rdd


class Song(object):
    def __init__(self):
        self.aes = myAES()
        # 防止请求过于频繁，用于请求间隔时间
        self.sleep_time = 0.005
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "referer": "https://music.y444.cn/",
        }

    # 当type=1时，表示post请求，为0时表示get请求
    def request_data(self, url, data={}, requestType=0):
        response = None
        if requestType:
            response = requests.post(url, data, headers=self.headers)
        else:
            response = requests.get(url, headers=self.headers)
        if response.status_code == 200 and response.json().get('data'):
            return response.json().get("data")
        else:
            print("请求失败")
            return ""

    def search_song_Byname(self, name, page=1, size=15):
        """
        :param name: 需要搜索的歌手名或者歌曲名
        :param page: 当前搜索的第几页
        :param size: 需要返回的数据大小
        :return: 歌曲信息(包括歌手信息，歌曲信息等)
        """
        url = "https://music.y444.cn/api/v1/search/v3/?keyword={}&page={}&size={}&src=kw".format(name, page, size)
        time.sleep(self.sleep_time)
        result = self.request_data(url)
        result = json.loads(self.aes.decrypt(result))
        data = []
        if len(result) == 0:
            return data
        print(result)
        for song in result.get("list"):
            row_data = dict()
            row_data["song_name"] = song["name"]
            row_data["song_url"] = self.get_song_url_by_id(song["id"])
            row_data["songer"] = song["author"]
            # todo 歌词暂未返回
            # row_data["song_lrc"] = self.get_song_lrc_by_id(song["id"], song["name"], song["author"])
            data.append(row_data)
        return data

    def get_song_url_by_id(self, songId=0):
        """
        :param songId: 歌曲id
        :return: 歌曲mp3路径
        """
        text = {
            "filename": "",
            'id': songId,
            'play': 'true',
            'q': "128",
            'src': "kw",
        }
        params = self.aes.encrypt(text)
        url = "https://music.y444.cn/api/v1/jx/v4/"
        data = {
            "sec_key": self.aes.sec_key,
            "params": params
        }
        time.sleep(self.sleep_time)
        result = self.request_data(url, data, 1)
        result = json.loads(self.aes.decrypt(result))
        return result.get("url").get("remote")

    def get_song_lrc_by_id(self, songId=0, songName="", songEr=""):
        url = "https://music.y444.cn/api/v1/search/lyric/lrc?id={}&src=kw&name={}".format(songId, songName + '-' + songEr)
        result = requests.get(url, headers=self.headers)
        return result.text


def work(key):
    return Song().search_song_Byname(key)


if __name__ == '__main__':
    # key = "周杰伦"
    # work(key)
    # data = get_song_url_by_id()
    # print(aes_dencrypt(data['data']))
    song = Song()
    print(song.search_song_Byname("搁浅"))
