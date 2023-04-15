#モジュールのインポート
import PIL.Image
import PIL.ImageFilter
import numpy
import cv2
import tkinter.filedialog as fd
import pathlib
import datetime


#ダイアログにて合成のもととなる画像を指定
img1_load = fd.askopenfilename(title="左側の画像を選択して下さい",initialdir="./blog_image", filetypes=[("JPGファイル",".jpg")])
img2_load = fd.askopenfilename(title="中央の画像を選択して下さい",initialdir="./blog_image", filetypes=[("JPGファイル",".jpg")])
img3_load = fd.askopenfilename(title="右側の画像を選択して下さい",initialdir="./blog_image", filetypes=[("JPGファイル",".jpg")])

#指定した画像をPILにて読み込む
img1 = PIL.Image.open(img1_load)
img2 = PIL.Image.open(img2_load)
img3 = PIL.Image.open(img3_load)

#各画像の幅と高さを読み込む
wid1, hei1 = img1.size
wid2, hei2 = img2.size
wid3, hei3 = img3.size

#ベースとなる背景が白の画像を作成
#幅：　（左の画像＋中央の画像＋右の画像）　ー　｛（左の画像＋中央の画像) * 0.1｝
#高さ：　左の画像
base_image00 = numpy.zeros((hei1, wid1+wid2+wid3-int((wid1+wid2)*0.1), 3))
base_image00 += 255
cv2.imwrite("base_image00.jpg", base_image00)
img4 = PIL.Image.open('base_image00.jpg')

#ベース画像に左の画像を右の画像を重ね合わせ、最後に中央の画像を重ね合わせる
img4.paste(img1, (0,0))
img4.paste(img3, (wid1+wid2-int((wid1+wid2)*0.1),0))
img4.paste(img2, (wid1-int(wid1*0.1),0))


#保存用フォルダを作成
out_folder = pathlib.Path("blog_gousei_image")
out_folder.mkdir(exist_ok=True)

#ファイル名に指定する現在日付を取得(YYYYMMDD形式)
dt_now = datetime.datetime.now()
dt_str = dt_now.strftime('%Y%m%d')

#保存ファイル名を指定
image_after_name = dt_str + "_2011_humannade_three_gousei.jpg"
out_path = out_folder.joinpath(image_after_name)

#画像を保存
img4.save(out_path, quality=95)

#完成画像を表示
img4.show()
