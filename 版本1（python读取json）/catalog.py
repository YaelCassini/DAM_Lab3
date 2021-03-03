from flask import Flask, url_for, redirect, request
from flask import render_template
import os
import json
app = Flask(__name__)

#主页
@app.route('/')
def home():
    return walkThough(0)

#分类索引页
@app.route('/<index>')
# @app.route('/song/<index>')
def walkThough(index=""):
    return walkThough(0, index)


# @app.route('/song/<index>/<name>', methods=['post', 'get'])
@app.route('/<index>/<name>', methods=['post', 'get'])
def song(name='001', index=""):
    # print(name)
    music=MusicData()
    origin_path=".\static\src"   #资源所在路径
    music.index=index
    music.json_addr = 'src/' + index + "/" + name + '.json'

    if index=="all":
        index=""
        path=origin_path
    else:
        path = origin_path + "\\" + index

    for root, dirs, files in os.walk(path):
        split = "."
        # 遍历文件
        last_name=""
        now_name=""
        for filename in files:
            temp_name, category = os.path.splitext(filename)  # 分解文件扩展名
            if filename.endswith(".mp3"):
                now_name=temp_name
                if last_name==name:
                    music.next_addr="/"+index+"/"+temp_name
                if now_name==name:
                    music.last_addr="/"+index+"/"+last_name
                last_name=temp_name

    if music.last_addr=="/Chinese/":
         music.last_addr=""
    if music.next_addr == "/Chinese/":
         music.next_addr = ""

    if music.last_addr=="/Others/":
         music.last_addr=""
    if music.next_addr == "/Others/":
         music.next_addr = ""


    load_f=open("./static/"+music.json_addr, "r")
    load_dict = json.load(load_f)

    music.name=load_dict['title']
    music.singer=load_dict['singer']
    music.CD=load_dict['CD']

    music.mp3_addr=load_dict['music_addr']
    music.pic_addr=load_dict['pic_addr']

    music.singer_addr = load_dict['singer_addr']
    music.CD_addr = load_dict['CD_addr']

    return render_template('music.html', name=name, musicdata=music)


#歌手页面
@app.route('/singer/<singer>')
def walkSinger(singer=""):
    return walkThough(4, "", singer)

#专辑页面
@app.route('/CD/<CD>')
def walkCD(CD=""):
    return walkThough(5, "", CD)

#搜索歌名
@app.route('/searchname', methods=['post', 'get'])
def search_name():
    return walkThough(1)

#搜索歌手
@app.route('/searchsinger', methods=['post', 'get'])
def search_singer():
    return walkThough(2)

#搜索专辑名
@app.route('/searchCD', methods=['post', 'get'])
def search_CD():
    return walkThough(3)

#0：没有选择条件
#1：查询歌名
#2：查询歌手
#3：查询专辑
#4：查看歌手
#5：查看歌名
#index：分类索引
#message：选择信息
def walkThough(choice=0, index="", message=""):
    datalist = []
    indexlist = []

    origin_path = ".\static\src"
    if index=="all":
        index=""
        path=origin_path
    else:
        path = origin_path + "\\" + index

    if choice==1:
        content = request.form.get('content')
    if choice==2:
        content = request.form.get('content2')
    if choice == 3:
        content = request.form.get('content3')

    for root, dirs, files in os.walk(origin_path):
        for d in dirs:
            dirname, basename = os.path.split(os.path.join(root, d))
            indexlist.append(basename)

    for root, dirs, files in os.walk(path):
        split = "."
        # 遍历文件
        for filename in files:
            filepath = os.path.join(root, filename)
            name, category = os.path.splitext(filename)  # 分解文件扩展名
            dirname, basename = os.path.split(filepath)
            tmp_ls = dirname.lstrip(origin_path)

            if filename.endswith(".mp3"):
                temp = Data()
                temp.index = tmp_ls
                temp.id=name
                temp.json_addr = "src/" + temp.index + "/" + name + ".json"

                # print("***")
                # print(name)

                load_f = open("./static/" + temp.json_addr, "r")
                load_dict = json.load(load_f)

                temp.html_addr = load_dict['html_addr']
                temp.pic_addr = load_dict['pic_addr']
                temp.music_addr = load_dict['music_addr']
                temp.name = load_dict['title']
                temp.singer = load_dict['singer']
                temp.CD = load_dict['CD']
                temp.singer_addr = load_dict['singer_addr']
                temp.CD_addr = load_dict['CD_addr']


                if choice==0:
                    datalist.append(temp)
                if choice==1:
                    if content in temp.name:
                        datalist.append(temp)
                if choice==2:
                    if content in temp.singer:
                        datalist.append(temp)
                if choice==3:
                    if content in temp.CD:
                        datalist.append(temp)
                if choice==4:
                    if temp.singer==message:
                        datalist.append(temp)
                if choice==5:
                    if temp.CD == message:
                        datalist.append(temp)

        # # 遍历所有的文件夹
        # for d in dirs:
        #     print(os.path.join(root, d))

    return render_template('catalog.html', datalist=datalist, indexlist=indexlist)


#catalog页面的数据类
class Data(object):
    index = ""
    pic_addr = ""
    music_addr = ""
    html_addr = ""
    name = ""
    singer = ""
    CD = ""
    json_addr=""
    id=""
    singer_addr = ""
    CD_addr = ""


#音乐信息类
class MusicData(object):
    last_addr=""
    next_addr=""
    json_addr=""
    index=""
    pic_addr =""
    mp3_addr=""
    singer_addr=""
    CD_addr=""


if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)