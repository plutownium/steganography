from PIL import Image
import sys

def rgb_to_hex(rgb):
    r,g,b = rgb
    return ('{:X}{:X}{:X}').format(r, g, b)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

#####################################
########## MAIN FUNCTION ############
#####################################


def main():
    IMAGE_FILE_NAME = "Dall-E 1_modified.png"
    PIXEL_SPACING = 300
    HEX_COLOR_INPUT = "#FF0000"



    ## Checking for command line inputs
    if(len(sys.argv) > 1):
        IMAGE_FILE_NAME = sys.argv[1]
        PIXEL_SPACING = int(sys.argv[2])
        HEX_COLOR_INPUT = sys.argv[3]

    
    HEX_COLOR_INPUT = rgb_to_hex(hex_to_rgb(HEX_COLOR_INPUT))
    im = Image.open(IMAGE_FILE_NAME)
    width, height = im.size
    total_pixels = width*height
    check_array = []

    for i in range(0,total_pixels,PIXEL_SPACING):
        y = i//width
        x = i - (y*width)
        # print(im.getpixel((x,y)))
        check_array.append(rgb_to_hex(im.getpixel((x,y))))

    print(HEX_COLOR_INPUT)
    # Check if all values in array match the specified value
    for i in check_array:
        print(i)
        if(i != HEX_COLOR_INPUT):
            print("Values of pixels do not match the input color specified")
            return
    print("All nth pixel values match the color value specified in the input!")

    

if __name__ == "__main__":
    main()