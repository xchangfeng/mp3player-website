# mp3 player website

## introduction
It is a full website that play music. All the music files are within the server of the website.

这是一个完整的播放器网站。为了建站方便，所有音频文件全在网站服务器内。


Now, it only suport .mp3 files and the music files are all in the mp3 folders. If you want to add more files, just upload your mp3 files into the mp3 folders. And the run the genelist.py to generate new list of the music list, which will be writtern to a javascript file: script.js.

目前，站点仅支持mp3文件，而且音频文件全在mp3文件夹内。如果你想增加其他的音乐文件，只需要向mp3文件夹上传文件，然后运行genelist.py来重新生成列表，这个会把列表写到js文件中。

Due to the size of this repositories, it just contain three songs. It could add more songs if you like.

由于代码库大小的问题，我们只放了三首歌。实际使用时，可以想放多少放多少。

## live demo
The live demo is on https://xiayuxi.com

## rely on
nginx / Apache

python package : eyed3 (https://github.com/nicfit/eyeD3)

## install
The simpe way to apply the website is like this. if there is no eyed3 package, when running `python3 genelist.py`, it would be an error. please install eyed3 first: `pip3 install eyed3`.


简单的步骤如下所示。如果没有eyed3包，那么在运行`python3 genelist.py`时会报错，那么应该先安装好eyed3包： `pip3 install eyed3`.


    cd /home/wwwroot  #the website play
    git clone https://github.com/xchangfeng/mp3player-website.git
    cd mp3player-website
    python3 genelist.py

Then, the configure file of nginx or apache need be changed to let the website work rightly.
   
然后还需要修改nginx或apache的配置文件，使得网页指向正确的位置。


## reference
This website was inpired by https://github.com/dylanbai8/V2Ray_ws-tls_Website_onekey. It only has one song on it. So it change it a litter bit to support more songs on it.


这个网站受这个项目启发：https://github.com/dylanbai8/V2Ray_ws-tls_Website_onekey. 但这上面只有一首歌，所以我稍做了一些变化，让它支持多首歌。

