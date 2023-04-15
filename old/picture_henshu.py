import pathlib
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageDraw
import datetime


#画像を読み込み、枠線を付ける
def image_waku(w_path):
    line_width = 80 #枠線の太さ
    waku_color = (240,240,240) #枠線の色
    src_im = PIL.Image.open(w_path)
    sw, sh = src_im.size
    cw, ch = sw + line_width * 2 , sh + line_width * 2
    canvas_im = PIL.Image.new('RGB', (cw, ch))
    canvas = PIL.ImageDraw.Draw(canvas_im)
    canvas.rectangle([(0, 0), (cw, ch)], fill=waku_color)
    canvas_im.paste(src_im, (line_width, line_width))
    return canvas_im

#大きさを70%に縮小する
def image_srink(path):
    #Image_road = image_waku(path)
    Image_road = path
    size = (round(Image_road.width * 0.7), round(Image_road.height * 0.7))
    Image_resize = Image_road.resize(size)
    return Image_resize

#読み込む画像を指定
load_image01 = fd.askopenfilename(title="読み込む画像1を指定",
                                  initialdir="./")
load_image02 = fd.askopenfilename(title="読み込む画像2を指定",
                                  initialdir="./")
load_image03 = fd.askopenfilename(title="読み込む画像3を指定",
                                  initialdir="./")

#画像1枠線を付ける
image01_waku = image_waku(load_image01)
#画像1を45°左に傾ける。expandをTrueにする事で、回転ではみ出した部分も表示する
#fillcolorにて背景色を白色にする
image01_rotate = image01_waku.rotate(30, expand=True, fillcolor=(255,255,255))
#画像縮小する
image01_resize = image_srink(image01_rotate)

#画像2枠線を付ける
image02_waku = image_waku(load_image02)
image02_resize = image_srink(image02_waku)

#画像3枠線を付ける
image03_waku = image_waku(load_image03)
#45°右に傾ける。expandをTrueにする事で、回転ではみ出した部分も表示する
#fillcolorにて背景色を白色にする
image03_rotate = image03_waku.rotate(-30, expand=True, fillcolor=(255,255,255))
image03_resize = image_srink(image03_rotate)

#保存用フォルダを作成
out_folder = pathlib.Path("blog_image")
out_folder.mkdir(exist_ok=True)

#保存ファイル名を指定
#画像ファイル末尾より、画像ファイル名を取得
af_imagename01 = load_image01.split("/")[-1]
af_imagename02 = load_image02.split("/")[-1]
af_imagename03 = load_image03.split("/")[-1]
#ファイル名に指定する現在日付を取得(YYYYMMDD形式)
dt_now = datetime.datetime.now()
dt_str = dt_now.strftime('%Y%m%d')
#保存ファイル名を指定
image_after_name01 = dt_str + "_2011_humannade" + af_imagename01
image_after_name02 = dt_str + "_2011_humannade" + af_imagename02
image_after_name03 = dt_str + "_2011_humannade" + af_imagename03
out_path01 = out_folder.joinpath(image_after_name01)
out_path02 = out_folder.joinpath(image_after_name02)
out_path03 = out_folder.joinpath(image_after_name03)

#画像を保存
image01_resize.save(out_path01, quality=95)
image02_resize.save(out_path02, quality=95)
image03_resize.save(out_path03, quality=95)
