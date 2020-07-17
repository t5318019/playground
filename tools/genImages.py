import os

try:
    from PIL import Image
    from PIL import ImageColor
except ModuleNotFoundError:
    exit("請安裝 Python Imaging Library, 指令: pip install Pillow")


def main():
    """ 產生 148 個不同顏色的 PNG 圖片檔案 """
    current_dir = (os.path.abspath(os.path.dirname(__file__)))
    output_dir = current_dir + os.sep + "output"
    os.path.exists(output_dir) or os.mkdir(output_dir)
    for color_name in ImageColor.colormap:
        filename = output_dir + os.sep + color_name + ".png"
        if os.path.exists(filename):
            continue
        im = Image.new("RGB", (800, 600), color_name)
        im.save(filename)


if __name__ == "__main__":
    main()
