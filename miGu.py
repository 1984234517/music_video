import requests
import logging


class miGuSong:

    def sendRequest(self, url, para={}):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
            "Cookie": "WT_FPC=id=286924a25c6691b22c61684166760072:lv=1684229099143:ss=1684229099143; mgAppH5CookieId=4217401514-10ta8lb5951d4a0e87a9d97c0b127e-1684309269",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "channel": "014000D",
        }
        res = requests.get(url, params=para, headers=headers)
        if res.status_code == 200:
            return res
        else:
            logging.error("请求出错")
            exit(-1)

    def searchSong(self, keyword, page=1):
        url = "https://c.musicapp.migu.cn/v1.0/content/search_all.do"
        para = {
            "text": keyword,
            "pageNo": page,
            'pageSize': 20,
            'isCopyright': 1,
            'sort': 1,
            'searchSwitch': '{"song":1,"album":0,"singer":0,"tagSong":1,"mvSong":0,"bestShow":1}',
        }
        res = self.sendRequest(url, para)
        res = res.json()
        if res.get("code") != "000000":
            logging.error("获取出错")
            exit(-1)
        res = res.get("songResultData").get("result")
        # print(res)
        songIdList = list()
        for song in res:
            songIdList.append([song.get("contentId"), song.get("copyrightId"), song.get("name"), song.get("singers")[0].get("name")])
        return songIdList

    def getSongUrl(self, songInfo):
        url = "https://c.musicapp.migu.cn/MIGUM3.0/strategy/listen-url/v2.4"
        songList = list()
        for song in songInfo:
            para = {
                "contentId": song[0],
                "copyrightId": song[1],
                "resourceType": "2",
                "netType": "01",
                "toneFlag": "PQ",
                "scene": "",
                "lowerQualityContentId": song[0],
            }
            res = self.sendRequest(url, para).json()
            data = dict()
            if res.get("data"):
                data["song_name"] = song[2]
                data["songer"] = song[3]
                data["song_url"] = res.get('data').get('url')
                songList.append(data)
        return songList

    def main(self, kerword):
        songInfo = self.searchSong(kerword)
        songList = self.getSongUrl(songInfo)
        return songList

if __name__ == '__main__':
    mi = miGuSong()
    songInfo = mi.searchSong("陈奕迅")
    songList = mi.getSongUrl(songInfo)
    print(songList)
