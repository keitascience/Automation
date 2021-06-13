import glob
import os
 
# 拡張子.jpgのファイルを取得する
path = '*.jpg'
i = 1
 
# jpgファイルを取得する
flist = glob.glob(path)


name = input("車型・車番を入力してね")
 
# ファイル名を一括で変更する
for file in flist:
  os.rename(file, name + '_' + str(i) + '.jpg')
  i+=1
 

    
            


