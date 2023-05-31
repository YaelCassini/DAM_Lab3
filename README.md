# DAM_Lab3
json格式信息

0. 两个文件夹分别为两种json文件读取方式，其中第一种为用python文件读取后作为参数，在调用template函数时传入给html，第二种为将json文件的路径作为参数传给html，在html中引入jquery库，调用jquery语句打开json文件并调取数据，两种方式均能成功运行网站，并且分别进行了录屏展示，两种方式的源代码和资源文件以及录屏展示分别放在两个文件夹中。
1. 请将资源文件按照文件夹分类解压到 'static/src' 目录下。如图，Chinese和Others分别为第一次作业时收集的资源文件的两个分类。
2. 将文件夹作为python工程打开（请注意将工程文件移入没有中文的路径下，否则可能会运行失败），运行 “txt2json.py” ，即可将所有的txt中的信息提取出来并生成json文件，结果如图。
3. 运行 “catalog.py” ，即可在本机浏览器上打开音乐播放网页。网址http://127.0.0.1:5000。
4. 压缩包中， “catalog.py” 和“txt2json.py”为python源代码，template文件夹下的 “catalog.html” 和 “music.html” 分别为网页目录页和音乐播放页的html源代码。
5. 实验中发现，在打开音乐播放页面时，python函数song将会被调用两次，在第二种方式（即使用jquery打开并解析json文件）运行过程中，第二次调用会出现无法解析url路径的路径，产生报错，但并不影响网页运行结果。
