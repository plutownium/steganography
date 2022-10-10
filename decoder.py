from PIL import Image
import sys

def get_embedded_string_binary(im: Image, n: int):
    width, height = im.size 
    binary_string = []
    if(n<=0):
        for x in range(height):
            for y in range(width):
                r,g,_ = im.getpixel((x,y))
                binary_string.append(bin(r)[-2:])
                binary_string.append(bin(g)[-2:])
    else:
        count = 0
        n *= 8
        for x in range(height):
            for y in range(width):
                r,g,_ = im.getpixel((x,y))
                binary_string.append(bin(r)[-2:])
                binary_string.append(bin(g)[-2:])
                count += 4
                if(count>=n):
                    break
            if(count>=n):
                break
    return "".join(binary_string)


def binary_to_ascii(binary_string):
    ascii_string = []
    for i in range(0,len(binary_string),8):
        temp = binary_string[i:i+8]
        if temp.isnumeric() and int(temp,2)<127:
            ascii_string.append(chr(int(temp,2)))

    return "".join(ascii_string)






def main():
    image_path = "temp.png"
    string_length = 0
    
    if(len(sys.argv)>1):
        image_path = sys.argv[1]
        string_length = int(sys.argv[2])

    im = Image.open(image_path)
    embedded_string_binary = get_embedded_string_binary(im, string_length)
    ascii_string = binary_to_ascii(embedded_string_binary)
    print(ascii_string)




if __name__ == "__main__":
    main()