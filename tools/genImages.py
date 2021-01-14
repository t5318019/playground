import os

try:
    from PIL import Image
    from PIL import ImageColor
except ModuleNotFoundError:
    exit("請安裝 Python Imaging Library 7.2.0, 指令: pip install Pillow")


def main():
    """ 產生 148 個不同顏色的 PNG, JPEG, GIF 圖片檔案 """
    current_dir = (os.path.abspath(os.path.dirname(__file__)))
    image_types = ("png", "jpg", "gif")

    for image_type in image_types:
        output_dir = current_dir + os.sep + "output" + os.sep + image_type
        os.makedirs(output_dir, exist_ok=True)

        for color_name in ImageColor.colormap:
            im = Image.new("RGB", (800, 600), color_name)
            filename = output_dir + os.sep + color_name + "." + image_type
            if not os.path.exists(filename):
                im.save(filename)

    """ 產生不同大小的 JPEG 圖片 """
    output_dir = current_dir + os.sep + "output" + os.sep + "size"
    os.makedirs(output_dir, exist_ok=True)

    sizes = (
        (320, 240),
        (640, 480),
        (800, 600),
        (1024, 768),
        (2048, 1536),
        (640, 360),
        (1280, 720),
        (1920, 1080),
        (2560, 1440),
        (3840, 2460),
        (7680, 4320),
        (15360, 8640),
    )

    for size in sizes:
        im = Image.new("RGB", size, "cyan")
        filename = output_dir + os.sep + "{}x{}.jpg".format(*size)
        if not os.path.exists(filename):
            im.save(filename)


if __name__ == "__main__":
    main()
