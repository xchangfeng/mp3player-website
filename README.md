# mp3 player website

## introduction
It is a full website that playing mp3 music. All the music files are saved on the server of the website.

这是一个完整的mp3音乐播放器网站。所有音频文件都保存在网站服务器内。


Now, it only suport .mp3 file and the music files are all in the “mp3” folders. If you want to add more files, just upload your mp3 files into the “mp3” folders. And the run the genelist.py to generate a new list of the music, which will be writtern to a javascript file: script.js.

目前，站点仅支持mp3文件，且音频文件全在mp3文件夹内。如果你想增加音乐，只需将这些文件上传到mp3文件夹，然后运行genelist.py来重新生成列表，这一步会把列表写到js文件(script.js)中。

Due to the size of this repositories, it only contain three songs. Actually，you add as much songs as possible according the size of storage.

由于代码库大小的问题，我们只放了三首歌。实际使用时，可以根据存储空间大小想放多少放多少。

## live demo
The live demo is on https://xiayuxi.com

实时的演示网站位于：https://xiayuxi.com

## rely on
nginx / Apache

python package : eyed3 (https://github.com/nicfit/eyeD3)

## install
The simpe way to apply the website is as following. If there is no eyed3 package, when running `python3 genelist.py`, it would be an error. please install eyed3 first: `pip3 install eyed3`.


简单的步骤如下所示。如果没有eyed3包，那么在运行`python3 genelist.py`时会报错，那么应该先安装好eyed3包： `pip3 install eyed3`.


    cd /home/wwwroot  #the website play
    git clone https://github.com/xchangfeng/mp3player-website.git
    cd mp3player-website
    python3 genelist.py

Then, the configure file of nginx or apache related to let the website work rightly.
   
然后还需要修改nginx或apache的配置文件，使得网页指向正确的位置。


## reference
This website was inpired by https://github.com/dylanbai8/V2Ray_ws-tls_Website_onekey. It only has one song on it. It was changed a litter bit to support more songs on it.


这个网站受这个项目启发：https://github.com/dylanbai8/V2Ray_ws-tls_Website_onekey. 但这上面只有一首歌，所以我稍做了一些变化，让它支持多首歌。

