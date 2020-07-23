import os

try:
    from PIL import Image
    from PIL import ImageColor
except ModuleNotFoundError:
    exit("請安裝 Python Imaging Library 7.2.0, 指令: pip install Pillow")


def main():
    """ 產生 148 個不同顏色的 PNG, JPEG 圖片檔案 """
    current_dir = (os.path.abspath(os.path.dirname(__file__)))
    output_png_dir = current_dir + os.sep + "output" + os.sep + "png"
    output_jpg_dir = current_dir + os.sep + "output" + os.sep + "jpg"
    os.makedirs(output_png_dir, exist_ok=True)
    os.makedirs(output_jpg_dir, exist_ok=True)
    for color_name in ImageColor.colormap:
        im = Image.new("RGB", (800, 600), color_name)

        png_filename = output_png_dir + os.sep + color_name + ".png"
        if not os.path.exists(png_filename):
            im.save(png_filename)

        jpg_filename = output_jpg_dir + os.sep + color_name + ".jpg"
        if not os.path.exists(jpg_filename):
            im.save(jpg_filename)


if __name__ == "__main__":
    main()
