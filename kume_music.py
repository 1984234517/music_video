import requests
from urllib import parse
from pprint import pprint
import urllib

def get_html(url, keyword, data={}):
    key = {
        'key': keyword
    }
    headers = {
        'Referer': 'https://www.kuwo.cn/search/list?'+parse.urlencode(key),
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.2.164445937.1647530868; _gid=GA1.2.53005613.1647530868; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1647530868; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1647530868; kw_token=03Q23V0RUXJO; _gat=1',
        'csrf': '03Q23V0RUXJO',
        'Host': 'kuwo.cn',
        'Pragma': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    print(res.status_code, '状态码为')
    if res.status_code == 200:
        return res
    else:
        print(res.text)
        print('获取歌曲信息出错，请重试')
        exit(0)

def get_song_info(keyword, song_size=30):
    url = 'https://kuwo.cn/api/www/search/searchMusicBykeyWord'
    data = {
        'key': keyword,
        'pn': '1',
        'rn': song_size,
        'httpsStatus': '1',
        'reqId': 'e3300640-a607-11ec-910f-cd33d72d1993',
    }
    url = url +'?'+parse.urlencode(data)
    print(url)
    try:
        res = get_html(url, keyword).json()
        song_data = res['data']['list']
        song_name = []
        songer_name = []
        song_rid = []
        for key in song_data:
            songer_name.append(key['artist'])
            song_name.append(key['name'])
            song_rid.append(key['rid'])
        # print(song_name)
        # print(songer_name)
        # print(len(song_rid))
        return song_name, songer_name, song_rid
    except:
        print('23获取歌曲信息出错')
        exit(0)

def download_song(song_url, song_name, songer_name):
    try:
        for i in range(len(song_url)):
            filename = songer_name[i] +'_'+ song_name[i] + '.mp3'
            if song_url[i]:
                urllib.request.urlretrieve(song_url[i],filename)
                print(filename, '下载完成')
            else:
                print(filename, '歌曲下载失败')
    except:
        print('下载出错了')
        exit(0)

def get_song_url(song_rids, keyword):
    song_url = []
    for song_rid in song_rids:
        if song_rid:
            url = 'https://kuwo.cn/api/v1/www/music/playUrl'
            # br这里表示的音乐的品质，共有三个等级[ "320kmp3", "192kmp3", "128kmp3" ]
            # data = {
            #     'format': 'mp3',
            #     'rid': song_rid,
            #     'response': 'url',
            #     'type': 'convert_url3',
            #     'br': '320kmp3',
            #     'from': 'web',
            #     't': '1598926556988',
            #     'httpsStatus': '1',
            #     'reqId': '12047ed1-ebf9-11ea-90b1-bdd0259e4026',
            # }
            data = {
                'mid': song_rid,
                'type': 'music',
                'httpsStatus': '1',
                'reqId': '5e8f7861-a609-11ec-910f-cd33d72d1993',
            }
            url = url+'?'+parse.urlencode(data)
            res = get_html(url, keyword).json()
            # print(res)
            if(res.get('code') and res['code']==-1):
                print(res['msg'])
                exit(0)

            song_url.append(res['data']['url'])
        else:
            print('该歌曲播放url获取失败')
            continue
    return song_url
def kume(keyword):
    song_name, songer_name, song_rid = get_song_info(keyword)
    song_url = get_song_url(song_rid, keyword)
    resulst = []
    for i in range(len(songer_name)):
        temp = dict()
        temp['song_name'] = song_name[i]
        temp['song_url'] = song_url[i]
        temp['songer'] = songer_name[i]
        resulst.append(temp)
    return resulst

if __name__ == '__main__':
    keyword = input('请输入你想要下载的歌曲名或者是歌手名字')
    print(kume(keyword))