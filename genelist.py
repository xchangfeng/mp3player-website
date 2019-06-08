import eyed3
import os
import re
#help(eyed3)
mp3path = "./mp3/"
imgpath = "./img/"
jsfile = "./js/script.js"
#先生成一个临时文件存储列表
flist = open("list.txt","w")

files = os.listdir(mp3path)
#列出所有文件，逐个生成mp3的信息，包括title, artist, album, cover picture,即mp3文件自带的图像。
for f in files:
  #print(mp3path + f)
  #是mp3再处理相关程序
  if os.path.splitext(f)[1] == ".mp3" :
    mySong = eyed3.load(mp3path + f)
    #print("title:" + re.escape(mySong.tag.title))
    flist.writelines("{")
    flist.write("\n")
    flist.writelines("title:" + "'" + re.escape(mySong.tag.title) + "',")
    flist.write("\n")
    flist.writelines("artist:" + "'" + re.escape(mySong.tag.artist) + "',")
    flist.write("\n")
    flist.writelines("album:" + "'" + re.escape(mySong.tag.album) + "',")
    flist.write("\n")  
    #如果存在照片，则把照片存到img用于显示，如果没有的话，就用默认的3.jpg做封面
    #print(len(mySong.tag.images))
    if len(mySong.tag.images) > 0:
      #print(mySong.tag.images.get("").description)
      #print(mySong.tag.images.get("").picture_type)
      #print(mySong.tag.images.get("").mime_type)
      #print(mySong.tag.images.get("")._mime_type)
      #本来是根据信息来区分jpg和png,但目前信息上没区分，只能用png的头来区分一下。
      if mySong.tag.images.get("").image_data[0] == 0x89 and mySong.tag.images.get("").image_data[1] == 0x50 :
        writepath = imgpath + os.path.splitext(os.path.basename(f))[0] + ".png"
      else:
        writepath = imgpath + os.path.splitext(os.path.basename(f))[0] + ".jpg"
       #print(writepath)
      fp = open(writepath,"wb")
      fp.write(mySong.tag.images.get("").image_data)
      fp.close()
      flist.writelines("cover:" + "'" + re.escape(writepath[2:]) + "',")
      flist.write("\n")
    else:
      flist.writelines("cover:" + "'" +"img/3.jpg" + "',")
      flist.write("\n")
    flist.writelines("mp3:" + "'" + re.escape(mp3path[2:] + f) + "',")
    flist.write("\n")
    flist.writelines("ogg:" + "'" + "',")
    flist.write("\n")
    flist.writelines("},")
    flist.write("\n")
flist.close()
#生成列表完成后，放到原来的js文件中间，位置是playlist = [ 和 ]; 之间。后面位置+13是为了保证playlist这行还在。
forigin = open(jsfile,"r")
jscontent = forigin.read()
flist = open("list.txt","r")
content_add = flist.read() 
flist.close()
forigin.close()
pos_start = jscontent.find("playlist = [")
pos_end = jscontent.find("];")
#print(pos_start)
#print(pos_end)
if pos_start != -1 and pos_end != -1:  
        content = jscontent[:pos_start + 13] + content_add + jscontent[pos_end:]  
        file = open( jsfile, "w" )  
        file.write( content )   

        file.close()  
         

