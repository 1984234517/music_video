import requests,urllib
import json

def get_url (url,data):
    data = urllib.parse.urlencode(data)
    url = url + '?' + data
    return url

def get_mid(url,key,number):
    mid_item = []
    song_name = []
    songer_item = []
    # data = {
    #     'ct': '24',
    #     'new_json': '1',
    #     'remoteplace': 'txt.yqq.song',
    #     'searchid': '63682231781232894',
    #     't': '0',
    #     'aggr': '1',
    #     'cr': '1',
    #     'catZhida': '1',
    #     'lossless': '0',
    #     'flag_qc': '0',
    #     'p': '1',
    #     'n': number,
    #     'w': key,
    #     'format': 'json',
    # }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'cookie': 'pgv_pvi=4768345088; pgv_pvid=883619592; tvfe_boss_uuid=5ed042a427945476; RK=B+R5s8nfXk; ptcz=f99a654e73b9b2493d366ed871ced0490b314d4c39eb8cd59be0ae4024705f21; o_cookie=1984234517; pac_uid=1_1984234517; iip=0; fqm_pvqid=502516cc-654d-4d6a-9c11-5a4c8ad6328f; ts_uid=2279619110; Qs_lvt_323937=1612407194%2C1612407200%2C1616842245%2C1627038266%2C1628946416; Qs_pv_323937=2175772846366405600%2C1436884701231862300%2C4382048082303364000%2C43523544994987810%2C1226353113946275000; LW_sid=h156E3H5g8L6e0C320s1L8o9l8; pgv_info=ssid=s1691875925; vversion_name=8.2.95; video_omgid=1af0b91f5ebdc829; fqm_sessionid=3ab17df4-0b54-41e7-8b92-e2adc5b11438; ts_last=y.qq.com/; ts_refer=cn.bing.com/',
        'accept': 'application/json',
        'authority': 'c.y.qq.com',
        'method': 'GET',
        'path': '/splcloud/fcgi-bin/smartbox_new.fcg?_=1647576339349&cv=4747474&ct=24&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=1&uin=0&g_tk_new_20200303=5381&g_tk=5381&hostUin=0&is_xml=0&key={}'.format(song_name),
        'scheme': 'https',
        'accept': 'application/json',
        'origin': 'https://y.qq.com',
        'pragma': 'no-cache',
        'referer': 'https://y.qq.com/',
    }
    url = 'https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?_=1647576339349&cv=4747474&ct=24&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=1&uin=0&g_tk_new_20200303=5381&g_tk=5381&hostUin=0&is_xml=0&key={}'.format(key)
    print(url)
    respond = requests.get(url, headers=headers)
    # print('源json文件为',respond.text)
    information = json.loads(respond.text)
    print(information)
    song = information.get('data').get('song').get('itemlist')
    length = len(song)
    # print('长度为',length)
    for i in range(length):
        mid_item.append(song[i].get('mid'))
        song_name.append(song[i].get('name'))
        print(song[i].get('name'))
        songer_item.append(song[i].get('singer'))
    return mid_item,song_name,songer_item

# 获取歌曲的下载地址
def get_song_url(url,mid):
    data1 = {
        '-': 'getplaysongvkey27834733422062374',
        'g_tk': '177848969',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'platform': 'yqq.json',
        'needNewCode': '0',
    }
    url_one = get_url(url, data1)
    # print("mid的长度为",len(mid))
    song_url = []
    for i in mid:
        data = {"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"8147203620","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8147203620","songmid":[i],"songtype":[0],"uin":"1984234517","loginflag":1,"platform":"20"}},"comm":{"uin":1984234517,"format":"json","ct":24,"cv":0} }
        print('数据为',data)
        url = url_one+'&data='+json.dumps(data)
        respond = requests.get(url=url)
        information = json.loads(respond.text)
        qian_url = information.get('req_0').get('data').get('sip')[0]
        information = information.get('req_0').get('data').get('midurlinfo')
        if information:
            information = information[0]
            hou_url = information.get('purl')
            url = qian_url+hou_url
            song_url.append(url)
            print("歌曲url为",url)
    return song_url
# 主函数
def get_song(song_key):
    url = 'https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg'
    number = 25
    song_infon = []
    mid_item, song_name, songer_item = get_mid(url, song_key, number)
    vkey_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg'
    song_item = get_song_url(vkey_url, mid_item)
    for i in range(len(song_name)):
        result = {}
        print('歌曲信息为', song_item[i], song_name[i])
        result['song_url'] = song_item[i]
        result['song_name'] = song_name[i]
        result['songer'] = songer_item[i]
        song_infon.append(result)
    print(song_infon)
    return song_infon

if __name__ == '__main__':
    # key = '张杰'
    # url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?'
    # number = '100'
    # mid_item ,song_name= get_mid(url,key,number)
    # vkey_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg'
    # get_song_url(vkey_url,mid_item)
    get_song('张杰 天下')