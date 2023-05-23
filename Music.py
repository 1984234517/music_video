from flask import Flask, render_template, request, jsonify
from decoder2 import wangyi
from kume_music import kume
from Ku_Dog import ku_dog
from xiage import Song
from qq_music import get_song
from get_video import get_aim_video
from yocool import get_deatil
from miGu import miGuSong
import logging as log
from get_video_2 import Video
app = Flask(__name__)

# 默认音乐
@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('music_index.html')

# 视频页面
@app.route('/index/video', methods=['GET',  'POST'])
def video():
    if request.method == 'GET':
        return render_template('video.html', datas={})
    else:
        key_word = request.form.get('search_key')
        select_id = request.form.get('select_id')
        log.info('选择的播放器'+str(select_id))
        if select_id == '腾讯视频':
            video_data_item = Video().search_by_name(key_word)
            if len(video_data_item) == 0:
                data = {'statu': '0', 'info': '没有查到相关的信息，请重新输入你的选择'}
            else:
                data = {'statu': '1', 'info': video_data_item, 'length': len(video_data_item)}
        else:
            data = {'statu': '0', 'info': '没有查到相关的信息，请重新输入你的选择'}
        return render_template('video.html', datas=data)
@app.route('/index/search')
def search():
    key_vlaue = request.args.get('query_value')
    check_vlaue = request.args.get("type")
    log.info("选择的播放器是"+str(check_vlaue)+"请求参数是："+str(key_vlaue))
    if check_vlaue == '网易云音乐':
        song_url = wangyi(key_vlaue)
        if song_url != '':
            data = dict(data=song_url, statu=1)
            return jsonify(data)
    else:
        if check_vlaue == 'QQ音乐':
            song_id = get_song(key_vlaue)
        elif check_vlaue == '酷我音乐':
            song_id = kume(key_vlaue)
        elif check_vlaue == '酷狗音乐':
            song_id =ku_dog(key_vlaue)
        elif check_vlaue == "下载吧":
            song = Song()
            song_id = song.search_song_Byname(key_vlaue)
        elif check_vlaue == '咪咕音乐':
            mi = miGuSong()
            song_id = mi.main(key_vlaue)
        if song_id != '':
            data = dict(data=song_id, statu=0)
            return jsonify(data)
        else:
            return jsonify({})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
