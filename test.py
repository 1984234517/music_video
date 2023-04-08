import requests
from hyper.contrib import HTTP20Adapter
import time

def get():
    url = 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/56/74/184207456/184207456-1-30064.m4s'
    data ={
        'e': 'ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M =',
    'uipk': '5',
    'nbs': '1',
    'deadline': int(time.time()),
    'gen': 'playurl',
    'os': 'cosbv',
    'oi': '3748151238',
    'trid': '63b2cb3a5f1a4cf59b40c64d77a52429u',
    'platform': 'pc',
    'upsig': 'fee153c727b20d5986bfe8977111ea8b',
    'uparams': 'e, uipk, nbs, deadline, gen, os, oi, trid, platform',
    'mid': '494222848',
    'orderid': '0, 3',
    'agrr': '1',
    'logo': '80000000'
    }
    header = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/84.0.4147.105Safari/537.36',
        'referer': 'https://www.bilibili.com/video/BV1Mi4y1b7MQ?from=search&seid=8349626842020598982',
        'authority':'upos-sz-mirrorcos.bilivideo.com',
        'method': 'GET',
        'path': '/upgcxcode/56/74/184207456/184207456-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1596717869&gen=playurl&os=cosbv&oi=3748151238&trid=63b2cb3a5f1a4cf59b40c64d77a52429u&platform=pc&upsig=fee153c727b20d5986bfe8977111ea8b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=494222848&orderid=0,3&agrr=1&logo=80000000',
        'scheme': 'https',
    }
    sessions = requests.session()
    sessions.mount('https://upos-sz-mirrorcos.bilivideo.com', HTTP20Adapter())
    print(int(time.time()))
    res = requests.get(url,data = data,headers=header)
    print(res.status_code)

if __name__ == '__main__':
    get()