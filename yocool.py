import requests
import re

def get_html(url, data={}):
    headers = {
        'cookie': '__ysuid=155368167683669n; __yscnt=1; cna=rv2nF4o5RlICAXWIT45AyTVQ; _m_h5_tk=d1e2b7891503c56b8173a89f7c7b23b8_1603442884685; _m_h5_tk_enc=487272e59caa5c3e8fd73cd6d43d3510; UM_distinctid=175545fe87688-08b6a563ca0898-3c634103-100200-175545fe8772d8; __ayft=1603438416103; __aysid=1603438416104hoO; __ayscnt=1; P_ck_ctl=E720A1F5FEBBEF5EAB3E16F83399607E; xlly_s=1; ctoken=-77zOmMnCYnrvo3idR7wOSYu; modalFrequency={"UUID":"2"}; redMarkRead=1; __ayvstp=11; __aysvstp=11; youku_history_word=%5B%22%25E7%259E%2584%25E5%2587%2586%22%2C%22%25E7%25A7%25A6%25E6%2597%25B6%25E6%2598%258E%25E6%259C%2588%22%5D; tfstk=cQQRB_YiR-2oAfOA_gEmRIXBuYadaMrJK-vZJ5tRqhxEiuz7ys0PSNI6jqAteEFA.; l=eBPVYJ2gOpBPWKfLBO5Z-urza77TPIdf1sPzaNbMiInca6wPhh2aHNQV3vkMVdtjgtfmsetrpXmLXRH9Wc4LRAN9QRQv4jECJxv9-; isg=BMnJOAbp8uobLI_FP4RqA6Jn2PUjFr1IRhnqm2s_6bDKsurEs2QqGHqo8BYE6lWA; __arpvid=1603439791009G0K0Jl-1603439791083; __arycid=dw-3-00; __arcms=dw-3-00; __aypstp=15; __ayspstp=15',
        'referer': 'https://v.youku.com/v_show/id_XNDg5MDYzODk4OA==.html?spm=a2hbt.13141534.app.5~5!2~5!2~5~5~5!2~5~5!2~5!2~5!2~5~A!2&s=efbfbd5ac9aaefbfbd5b',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        return res
    else:
        print("访问出错了")

# 根据用户输入的电影或者电视名称来得到相应电影或者电视的详情
def get_deatil(key_word):
    url = 'https://so.youku.com/search_video/q_{}?searchfrom=1'.format(key_word)
    base_url = 'http://peng3.com/vip/?a=https%3A%2F%2F2.08bk.com%2F%3Furl%3D%0D%0A&url='
    base_url2 = 'http://5.nmgbq.com/2/?url='
    print(url)
    res = get_html(url).text
    # print(res)
    url_data = re.findall(r'item_JEHzf.*?title="(.*?)".*?<div class="box-mark_130JR">.*?href="(.*?)".*?lass="aplus', res, re.S)
    print(url_data)
    detail_info = list()
    for i in range(len(url_data)):
        detail_info.append([url_data[i][0], base_url+url_data[i][1]])
    return detail_info

if __name__ == '__main__':
    key_word = input('请输入你想看的电视剧的名字')
    print(get_deatil(key_word))