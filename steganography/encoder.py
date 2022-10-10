from PIL import Image
import sys

def string_to_ascii(s):
    temp = []
    for i in s:
        t = bin(ord(i))[2:]
        t = ("0"*(8-len(t))) + t
        temp.append(t)
    return "".join(temp)

def embed_text_in_image(im, text):
    width, height = im.size
    if((width*height*4)<(len(text)*8)):
        print("Error: Image is not large enough to embed message into")
        return
    x=0
    y=0
    for i in range(0,len(text),4):
        r,g,b = im.getpixel((x,y))
        r = int(bin(r)[2:-2] + text[i:i+2],2)
        g = int(bin(g)[2:-2] + text[i+2:i+4],2)
        im.putpixel((x,y),(r,g,b))
        x+=1
        if(x>=width):
            y+=1
            x=0
    return im


def main():
    string_to_encode = "Hello World! This is a test string to be embedded in an image."
    image_path = "temp.jpg"

    if(len(sys.argv)>1):
        image_path = sys.argv[1]
        string_to_encode = sys.argv[2]

    binary_string = string_to_ascii(string_to_encode)
    im = Image.open(image_path)
    im = embed_text_in_image(im, binary_string)
    im.save(f"{image_path[:image_path.find('.')]}_modified.png")
    print(f"Image saved successfully as '{image_path[:image_path.find('.')]}_modified.png'")
    print(f"Note: The length of your string was: {len(string_to_encode)}")




if __name__ == "__main__":
    main()