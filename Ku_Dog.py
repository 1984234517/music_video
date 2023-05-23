import requests
import time
import hashlib
import execjs


def get_html(url, params):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'kg_mid=d81f643df388f5c5a513886589cb8641; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1598622040; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1598626763',
        'Host': 'complexsearch.kugou.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.kugou.com/yy/html/search.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
    }
    respon = requests.get(url, params=params, headers=headers)
    # get请求的参数写成params就好，不要写成data这样会出问题的
    if respon.status_code == 200:
        return respon
    else:
        print('请求出错')

# 原方案
def get_song_info(keyword,number=30):
    url = 'https://complexsearch.kugou.com/v2/search/song'
    data = str(int(time.time()*1000))
    a = 'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtbitrate=0callback=callback123clienttime={}clientver=2000dfid=-inputtype=0iscorrection=1isfuzzy=0keyword={}mid={}page=1pagesize={}platform=WebFilterprivilege_filter=0srcappid=2919tag=emuserid=-1uuid={}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'.format(data,keyword,data,number,data)
    js_code = """
    var singe = function(a) {
    function b(a) {
        var b = (a >>> 0).toString(16);
        return "00000000".substr(0, 8 - b.length) + b
    }
    function c(a) {
        for (var b = [], c = 0; c < a.length; c++)
            b = b.concat(k(a[c]));
        return b
    }
    function d(a) {
        for (var b = [], c = 0; 8 > c; c++)
            b.push(255 & a),
            a >>>= 8;
        return b
    }
    function e(a, b) {
        return a << b & 4294967295 | a >>> 32 - b
    }
    function f(a, b, c) {
        return a & b | ~a & c
    }
    function g(a, b, c) {
        return c & a | ~c & b
    }
    function h(a, b, c) {
        return a ^ b ^ c
    }
    function i(a, b, c) {
        return b ^ (a | ~c)
    }
    function j(a, b) {
        return a[b + 3] << 24 | a[b + 2] << 16 | a[b + 1] << 8 | a[b]
    }
    function k(a) {
        for (var b = [], c = 0; c < a.length; c++)
            if (a.charCodeAt(c) <= 127)
                b.push(a.charCodeAt(c));
            else
                for (var d = encodeURIComponent(a.charAt(c)).substr(1).split("%"), e = 0; e < d.length; e++)
                    b.push(parseInt(d[e], 16));
        return b
    }
    function l() {
        for (var a = "", c = 0, d = 0, e = 3; e >= 0; e--)
            d = arguments[e],
            c = 255 & d,
            d >>>= 8,
            c <<= 8,
            c |= 255 & d,
            d >>>= 8,
            c <<= 8,
            c |= 255 & d,
            d >>>= 8,
            c <<= 8,
            c |= d,
            a += b(c);
        return a
    }
    function m(a) {
        for (var b = new Array(a.length), c = 0; c < a.length; c++)
            b[c] = a[c];
        return b
    }
    function n(a, b) {
        return 4294967295 & a + b
    }
    function o() {
        function a(a, b, c, d) {
            var f = v;
            v = u,
            u = t,
            t = n(t, e(n(s, n(a, n(b, c))), d)),
            s = f
        }
        var b = p.length;
        p.push(128);
        var c = p.length % 64;
        if (c > 56) {
            for (var k = 0; 64 - c > k; k++)
                p.push(0);
            c = p.length % 64
        }
        for (k = 0; 56 - c > k; k++)
            p.push(0);
        p = p.concat(d(8 * b));
        var m = 1732584193
          , o = 4023233417
          , q = 2562383102
          , r = 271733878
          , s = 0
          , t = 0
          , u = 0
          , v = 0;
        for (k = 0; k < p.length / 64; k++) {
            s = m,
            t = o,
            u = q,
            v = r;
            var w = 64 * k;
            a(f(t, u, v), 3614090360, j(p, w), 7),
            a(f(t, u, v), 3905402710, j(p, w + 4), 12),
            a(f(t, u, v), 606105819, j(p, w + 8), 17),
            a(f(t, u, v), 3250441966, j(p, w + 12), 22),
            a(f(t, u, v), 4118548399, j(p, w + 16), 7),
            a(f(t, u, v), 1200080426, j(p, w + 20), 12),
            a(f(t, u, v), 2821735955, j(p, w + 24), 17),
            a(f(t, u, v), 4249261313, j(p, w + 28), 22),
            a(f(t, u, v), 1770035416, j(p, w + 32), 7),
            a(f(t, u, v), 2336552879, j(p, w + 36), 12),
            a(f(t, u, v), 4294925233, j(p, w + 40), 17),
            a(f(t, u, v), 2304563134, j(p, w + 44), 22),
            a(f(t, u, v), 1804603682, j(p, w + 48), 7),
            a(f(t, u, v), 4254626195, j(p, w + 52), 12),
            a(f(t, u, v), 2792965006, j(p, w + 56), 17),
            a(f(t, u, v), 1236535329, j(p, w + 60), 22),
            a(g(t, u, v), 4129170786, j(p, w + 4), 5),
            a(g(t, u, v), 3225465664, j(p, w + 24), 9),
            a(g(t, u, v), 643717713, j(p, w + 44), 14),
            a(g(t, u, v), 3921069994, j(p, w), 20),
            a(g(t, u, v), 3593408605, j(p, w + 20), 5),
            a(g(t, u, v), 38016083, j(p, w + 40), 9),
            a(g(t, u, v), 3634488961, j(p, w + 60), 14),
            a(g(t, u, v), 3889429448, j(p, w + 16), 20),
            a(g(t, u, v), 568446438, j(p, w + 36), 5),
            a(g(t, u, v), 3275163606, j(p, w + 56), 9),
            a(g(t, u, v), 4107603335, j(p, w + 12), 14),
            a(g(t, u, v), 1163531501, j(p, w + 32), 20),
            a(g(t, u, v), 2850285829, j(p, w + 52), 5),
            a(g(t, u, v), 4243563512, j(p, w + 8), 9),
            a(g(t, u, v), 1735328473, j(p, w + 28), 14),
            a(g(t, u, v), 2368359562, j(p, w + 48), 20),
            a(h(t, u, v), 4294588738, j(p, w + 20), 4),
            a(h(t, u, v), 2272392833, j(p, w + 32), 11),
            a(h(t, u, v), 1839030562, j(p, w + 44), 16),
            a(h(t, u, v), 4259657740, j(p, w + 56), 23),
            a(h(t, u, v), 2763975236, j(p, w + 4), 4),
            a(h(t, u, v), 1272893353, j(p, w + 16), 11),
            a(h(t, u, v), 4139469664, j(p, w + 28), 16),
            a(h(t, u, v), 3200236656, j(p, w + 40), 23),
            a(h(t, u, v), 681279174, j(p, w + 52), 4),
            a(h(t, u, v), 3936430074, j(p, w), 11),
            a(h(t, u, v), 3572445317, j(p, w + 12), 16),
            a(h(t, u, v), 76029189, j(p, w + 24), 23),
            a(h(t, u, v), 3654602809, j(p, w + 36), 4),
            a(h(t, u, v), 3873151461, j(p, w + 48), 11),
            a(h(t, u, v), 530742520, j(p, w + 60), 16),
            a(h(t, u, v), 3299628645, j(p, w + 8), 23),
            a(i(t, u, v), 4096336452, j(p, w), 6),
            a(i(t, u, v), 1126891415, j(p, w + 28), 10),
            a(i(t, u, v), 2878612391, j(p, w + 56), 15),
            a(i(t, u, v), 4237533241, j(p, w + 20), 21),
            a(i(t, u, v), 1700485571, j(p, w + 48), 6),
            a(i(t, u, v), 2399980690, j(p, w + 12), 10),
            a(i(t, u, v), 4293915773, j(p, w + 40), 15),
            a(i(t, u, v), 2240044497, j(p, w + 4), 21),
            a(i(t, u, v), 1873313359, j(p, w + 32), 6),
            a(i(t, u, v), 4264355552, j(p, w + 60), 10),
            a(i(t, u, v), 2734768916, j(p, w + 24), 15),
            a(i(t, u, v), 1309151649, j(p, w + 52), 21),
            a(i(t, u, v), 4149444226, j(p, w + 16), 6),
            a(i(t, u, v), 3174756917, j(p, w + 44), 10),
            a(i(t, u, v), 718787259, j(p, w + 8), 15),
            a(i(t, u, v), 3951481745, j(p, w + 36), 21),
            m = n(m, s),
            o = n(o, t),
            q = n(q, u),
            r = n(r, v)
        }
        return l(r, q, o, m).toUpperCase()
    }
    var p = null
      , q = null;
    return "string" == typeof a ? p = k(a) : a.constructor == Array ? 0 === a.length ? p = a : "string" == typeof a[0] ? p = c(a) : "number" == typeof a[0] ? p = a : q = typeof a[0] : "undefined" != typeof ArrayBuffer ? a instanceof ArrayBuffer ? p = m(new Uint8Array(a)) : a instanceof Uint8Array || a instanceof Int8Array ? p = m(a) : a instanceof Uint32Array || a instanceof Int32Array || a instanceof Uint16Array || a instanceof Int16Array || a instanceof Float32Array || a instanceof Float64Array ? p = m(new Uint8Array(a.buffer)) : q = typeof a : q = typeof a,
    q && alert("MD5 type mismatch, cannot process " + q),
    o()
}
    """
    singe = execjs.compile(js_code).call('singe', a)
    kk = {
        'callback': 'callback123',
        'keyword': keyword,
        'page': '1',
        'pagesize': number,
        'bitrate': '0',
        'isfuzzy': '0',
        'tag': 'em',
        'inputtype': '0',
        'platform': 'WebFilter',
        'userid': '-1',
        'clientver': '2000',
        'iscorrection': '1',
        'privilege_filter': '0',
        'srcappid': '2919',
        'clienttime': data,
        'mid': data,
        'uuid': data,
        'dfid': '-',
        'signature': singe
    }
    # url  = url+'?'+parse.urlencode(kk)
    # print(url)
    # res = get_html(url)
    # print(res.text)
    try:
        res = get_html(url, kk).text[12:-2]
        song_info = eval(res)
        song_info = song_info['data']['lists']
        song_hash_id = []
        song_name = []
        for i in song_info:
            song_hash_id.append((i['AlbumID'], i['FileHash']))
            song_name.append(i['FileName'])
        return song_hash_id, song_name
    except:
        print('获取歌曲信息出错了')
        exit(0)

# md5加密
def encryMd5(text):
    # 创建md5对象
    hl = hashlib.md5()

    # Tips
    # 此处必须声明encode
    # 若写法为hl.update(str) 报错为： Unicode-objects must be encoded before hashing
    hl.update(text.encode(encoding='utf-8'))
    return hl.hexdigest()

#　现方案
def getSongInfo(keyword,number=30):
    url = "https://complexsearch.kugou.com/v2/search/song"
    currentTime = int(time.time()*1000)
    encryData = 'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014bitrate=0callback=callback123clienttime={}clientver=1000dfid=3exjle1Za6nC43jwQx38vNTgfilter=10inputtype=0iscorrection=1isfuzzy=0keyword={}mid=8dd89fe11afd55a15b4f4aa87a4c08f1page=1pagesize={}platform=WebFilterprivilege_filter=0srcappid=2919token=userid=0uuid=8dd89fe11afd55a15b4f4aa87a4c08f1NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'.format(currentTime, keyword, number)
    signature = encryMd5(encryData)
    kk = {
        'callback': 'callback123',
        'srcappid': '2919',
        'clientver': '1000',
        'clienttime': currentTime,
        'mid': "8dd89fe11afd55a15b4f4aa87a4c08f1",
        'uuid': "8dd89fe11afd55a15b4f4aa87a4c08f1",
        'dfid': '3exjle1Za6nC43jwQx38vNTg',
        'keyword': keyword,
        'page': '1',
        'pagesize': number,
        'bitrate': '0',
        'isfuzzy': '0',
        'inputtype': '0',
        'platform': 'WebFilter',
        'userid': '0',
        'iscorrection': '1',
        'privilege_filter': '0',
        'filter': '10',
        'token': "",
        "appid": "1014",
        'signature': signature
    }
    try:
        res = get_html(url, kk).text[12:-2]
        song_info = eval(res)
        song_info = song_info['data']['lists']
        song_hash_id = []
        song_name = []
        for i in song_info:
            song_hash_id.append((i['AlbumID'], i['FileHash']))
            song_name.append(i['FileName'])
        return song_hash_id, song_name
    except:
        print('获取歌曲信息出错了')
        exit(0)
def get_song(song_hash_id, filename):
    url = 'https://wwwapi.kugou.com/yy/index.php'
    song_url = []
    for key in song_hash_id:
        data_time = str(int(time.time() * 1000))
        data = {
                'r': 'play/getdata',
                'hash': key[1],
                'album_id': key[0],
                'dfid': '1afTKN0wCGON0vaSW51z7hDZ',
                'mid': '3a163c18aaa274ca4d03ead24a84b5bf',
                'platid': '4',
                '_': data_time,
            }
        res = requests.get(url, params=data).json()
        if (res.get("status") == 0):
            continue
        song_url.append(res['data']['play_url'])
    print(song_url)
    result = []
    for i in range(len(song_url)):
        song_hash = dict()
        temp = filename[i].replace('/', '')
        temp = temp.replace('\\', '')
        temp = temp.replace('<em>', '')
        temp = temp.replace('<em>', '')
        temp = temp.split('-')
        if len(temp) == 2:
            song_hash['songer'], song_hash['song_name'] = temp[0], temp[1]
        else:
            song_hash['songer'], song_hash['song_name'] = '', ''
        song_hash['song_url'] = song_url[i]
        result.append(song_hash)
    return result


def ku_dog(keyword):
    song_hash_id, filename = getSongInfo(keyword)
    return get_song(song_hash_id, filename)