import json
import os

#Json文件的数据类
class Jsondata(object):
    id=""
    index = ""
    name = ""
    singer = ""
    CD = ""
    pubDate=""

    html_addr = ""
    pic_addr = ""
    music_addr = ""

    singer_addr = ""
    CD_addr = ""

    last_addr=""
    next_addr=""


def txt2json(addr=""):
    origin_path = addr  # 资源所在路径
    path=origin_path


    # if music.last_addr=="/Chinese/":
    #      music.last_addr=""
    # if music.next_addr == "/Chinese/":
    #      music.next_addr = ""
    #
    # if music.last_addr=="/Others/":
    #      music.last_addr=""
    # if music.next_addr == "/Others/":
    #      music.next_addr = ""

    last_name=""
    now_name=""
    # last_json_data

    for root, dirs, files in os.walk(path):
        split = "."
        # 遍历文件
        for filename in files:
            filepath = os.path.join(root, filename)
            name, category = os.path.splitext(filename)  # 分解文件扩展名
            dirname, basename = os.path.split(filepath)
            tmp_ls = dirname.lstrip(origin_path)


            if filename.endswith(".mp3"):
                temp = Jsondata()
                # if(now_name==""):
                #     temp.last_addr=""

                temp.index =tmp_ls
                temp.id=name
                txt_addr =temp.index +"/" +name +".txt"
                json_path=origin_path +"/" +temp.index +"/" +name +".json"

                temp.html_addr = "/" + temp.index + "/" + name
                temp.pic_addr = "src/" + temp.index + "/" + name + ".png"
                temp.music_addr = "src/" + temp.index + "/" + name + ".mp3"

                # 打开文件
                file =open(origin_path +"/" +txt_addr ,"r" ,encoding='UTF-8')
                lines = file.readlines()
                for line in lines:
                    # 提取发布日期
                    if line.startswith('\"pubDate\"', 0, len(line)):
                        i=0
                        str1 = ": "
                        index1 = line.find(str1, i, len(line))
                        i = index1+3
                        index2 = line.find(str1, i, len(line))
                        temp.date = line[index1 + 3:index2]

                    if line.startswith('\"description\"', 0, len(line)):
                        # 从txt文件中提取歌名
                        i = 0
                        str1 = "《"
                        str2 = "》"
                        index1 = line.find(str1, i, len(line))
                        index2 = line.find(str2, i, len(line))
                        temp.name = line[index1 + 1:index2]
                        i = index2

                        # 提取歌手
                        str1 = "由"
                        str2 = "演唱"
                        index1 = line.find(str1, i, len(line))
                        index2 = line.find(str2, i, len(line))
                        temp.singer = line[index1 + 2:index2 - 1]
                        i = index2

                        # 提取专辑名
                        str1 = "收录于《"
                        str2 = "》"
                        index1 = line.find(str1, i, len(line))
                        index2 = line.find(str2, i, len(line))
                        # 没有查找到后书名号
                        if index2 == -1:
                            index2 = len(line - 1)
                        temp.CD = line[index1 + 4:index2]

                temp.singer_addr = "/singer/" + temp.singer
                temp.CD_addr = "/CD/" + temp.CD

                json_data = {u'index': temp.index,
                        u'id': temp.id,
                        u'title': temp.name,
                        u'singer': temp.singer,
                        u'CD': temp.CD,
                        u'pubDate': temp.date,
                        u'html_addr': temp.html_addr,
                        u'pic_addr': temp.pic_addr,
                        u'music_addr': temp.music_addr,
                        u'singer_addr': temp.singer_addr,
                        u'CD_addr': temp.CD_addr,
                        }

                # 排序并缩进
                #json_temp=json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=2)
                json_temp = json.dumps(json_data, sort_keys=True, indent=2)

                # 新建json文件并写入信息
                #f = open(json_path,  'w', encoding = 'gb18030')
                f = open(json_path, 'w')
                f.write(json_temp)
                f.close()
    return


if __name__ == '__main__':
    addr=".\static\src"
    txt2json(addr)