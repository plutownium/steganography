Script 1 contains the code that changes the nth pixels to the specified values
and saves the file as `{ORIGINALFILENAME}_modified.png`. Script 2 contains the code
to check if the every nth pixel is indeed the color specified.

- The filename for the image is stored in a variable called `IMAGE_FILE_NAME`
- The value for pixel spacing is stored in a variable called `PIXEL_SPACING`
- The color value is stored in a variable called `HEX_COLOR_INPUT`

**NOTE: You can change these variables in the source code and run the script
        as `python3 script1.py`. You can also specify the values of the variables 
        as command line inputs. For both scripts, when running with command line inputs
        enter `python3 script1.py IMAGE_FILE_NAME PIXEL_SPACING HEX_COLOR_INPUT`
        e.g `python3 script1.py temp.png 300 ff0000`

**NOTE: Do NOT add a leading '#' symbol in front of your hex color value when entering it as
        a command line argument. (see example above)

**IMPORTANT: This works best with .png images (or other lossless formats). When using
             other image formats such as .jpg, since they undergo lossy compression,
             pixel values may (most probably will) change when saving the image. 