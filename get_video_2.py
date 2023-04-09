import requests
from urllib.parse import urlencode
import re
import logging as log

class Video():
    def __init__(self):
        self.headers = {
            "cookie": "pgv_pvi=4768345088; pgv_pvid=883619592; tvfe_boss_uuid=5ed042a427945476; video_platform=2; RK=B+R5s8nfXk; ptcz=f99a654e73b9b2493d366ed871ced0490b314d4c39eb8cd59be0ae4024705f21; o_cookie=1984234517; pac_uid=1_1984234517; iip=0; fqm_pvqid=502516cc-654d-4d6a-9c11-5a4c8ad6328f; _clck=16zt4p8|1|f5i|0; eas_sid=e166x7w0E7g5O3w020J9i149J2; video_guid=1af0b91f5ebdc829; pgv_info=ssid=s410575105; vversion_name=8.2.95; video_omgid=1af0b91f5ebdc829; _qpsvr_localtk=0.34857376079095115",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "origin": "https://v.qq.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        }
        self.pageInfo = ["need_async=true", "tab_id=1_100_198_0&need_async=true", "tab_id=1_199_297_0&need_async=true", "tab_id=1_298_396_0&need_async=true", "tab_id=1_397_495_0&need_async=true"]
        self.step = 99
    def search_by_name(self, name):
        url = "https://v.qq.com/x/search/?q={}".format(name)
        print(url)
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            # print(response.text)
            html = response.text
            try:
                data_id = re.search(r'data-id=\"([a-z,0-9]*)\"', html, re.S).group(1)
                all_number = re.search(r'<span class="figure_info">.*?(\d+).*?<', html, re.S).group(1)
            except Exception as e:
                log.error("获取集数出错", e)
                return []
        all_data = []
        log.info("总集数为"+all_number)
        for page in range(int(int(all_number)/self.step)+1):
            datas = self.get_list(data_id, page)
            for data in datas:
                all_data.append(data)
        return all_data

    def get_list(self, video_id, page=0):
        url = "https://pbaccess.video.qq.com/trpc.videosearch.search_cgi.http/load_playsource_list_info?"
        data = {
            "pageNum": 0,
            'id': video_id,
            'dataType': '2',
            'pageContext': self.pageInfo[page],
            'scene': '2',
            'platform': '2',
            'appId': '10718',
            'site': 'qq',
            'vappid': '34382579',
            'vsecret': 'e496b057758aeb04b3a2d623c952a1c47e04ffb0a01e19cf',
        }
        all_data = []
        url += urlencode(data)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            try:
                data = data["data"]["normalList"]["itemList"][0]["videoInfo"]["firstBlockSites"][0]["episodeInfoList"]
                log.info("第"+str(page)+"次请求数据长度为"+str(len(data)))
                index = 0
                for d in data:
                    # 片段时间小于35秒的认为是预告篇
                    if int(d.get("duration")) <= 45:
                        all_data.append(["预告"+d.get('title'), d.get("url")])
                    else:
                        all_data.append([d.get('title'), d.get("url")])
                    index += 1
            except Exception as e:
                log.error("数据读取失败", e)
                return all_data
        return all_data

if __name__ == '__main__':
    video = Video()
    print(video.search_by_name("斗破苍穹年番"))