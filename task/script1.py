from PIL import Image
import sys


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))



def main():
    IMAGE_FILE_NAME = "pp photo-removebg-preview_modified.jpg"
    PIXEL_SPACING = 300
    HEX_COLOR_INPUT = "#FF0000"

    ## Setting params from the command line
    if(len(sys.argv) > 1):
        IMAGE_FILE_NAME = sys.argv[1]
        PIXEL_SPACING = int(sys.argv[2])
        HEX_COLOR_INPUT = sys.argv[3]

    rgb = hex_to_rgb(HEX_COLOR_INPUT)

    # open image
    im = Image.open(IMAGE_FILE_NAME)
    width, height = im.size
    # print(width,height)
    total_pixels = width * height
    for i in range(0,total_pixels,PIXEL_SPACING):
        y = i//width
        x = i - (y*width)
        im.putpixel((x,y),rgb)

    im.save(f"{IMAGE_FILE_NAME[:IMAGE_FILE_NAME.find('.')]}_modified{IMAGE_FILE_NAME[IMAGE_FILE_NAME.find('.'):]}")

 




if __name__ == "__main__":
    main()
