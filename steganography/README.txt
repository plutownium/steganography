IMPORTANT: In both cases, the script expects to be run in the same
           folder as the images.

--------ENCODER-------
`encoder.py` contains the code to embed a string into an image.
It has two parameters: the image_path and the string to be encoded
You can choose to change these variables directly in the source code
or provide them as command line arguments as 
`python3 encoder.py image_path string`
e.g `python3 encoder.py picture.jpg Hello\ World!`

**Note: When adding spaces in the command line as part of a string,
        remember to escape them with a backslash `\`.

When the embedding is done, it returns a success message and also prints the 
number of characters in your embedded string (this number will be useful later.)

**Note: You can provide any kind of image including jpegs. The modified image will
        be saved as a png however.

--------DECODER---------
`decoder.py` contains the code to decode an embedded message from an image.
It has two parameters: the image_path and string_length
You can choose to change these variables directly in the source code
or provide them as command line arguments as 
`python3 decoder.py image_path string_length`
e.g `python3 decoder.py pic_modified.png 67`

This prints out the string embedded in the pixels.

**Note: You can also pass 0 as the string length. This will make it read each
        pixel until the end of the image. The output will start with the 
        embedded message, but will carry on with mostly gibberish until it 
        reaches the end of the image.
