'''
Created on Jul 17, 2018

@author: tevin
'''
#this module calculates the canopy coverage in the given picture:


from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def apply_filter(image, filter):
    '''
    Create and return a NEW image, based on a
    transform of each pixel in the given image using the given filter
    image is an open Image object
    filter is a function to apply to each pixel in image
    return new image, same size, to which filter has been applied to each pixel of image
    '''
    pixels = [ filter(p) for p in image.getdata() ]
    nim = Image.new("RGB",image.size)
    nim.putdata(pixels)
    return nim

def load_and_go(fname,filterfunc):
    image = open_image(fname)
    nimage = apply_filter(image,filterfunc)
    image.show()
    nimage.show()
    '''
    processedImage.jpg is the name of the file
    the image is saved in. The first time you do 
    this you may have to refresh to see it.
    '''
    nimage.save("processedImage.jpg")


def calculate(fname):
    #this function does the calculation
    image = open_image(fname)
    print( [p for p in image.getdata()][:50])
    pixels = [ canopyWhite(p) for p in image.getdata() ]
    canopypixels = pixels.count(1)
#     print(pixels)
    return canopypixels/len(pixels)
    
def canopyWhite(pixel):
    r,g,b = pixel
    str =""
    if r> 200:
        str += "y"
    if b>200:
        str += "es"
    if str == "yes":
        return 1
    else:
        return -1
     
def open_image(filename):
    '''
    opens the given image and converts it to RGB format
    returns a default image if the given one cannot be opened
    filename is the name of a PNG, JPG, or GIF image file
    '''
    image = Image.open(filename)
    if image == None:
        print("Specified input file " + filename + " cannot be opened.")
        return Image.new("RGB", (400, 400))
    else:
        print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
        return image.convert("RGB")
    
def greens(pixel):
    r,g,b = pixel
    return r,0,b

if __name__ == "__main__":
    ''' Change the name of the file and the function
        to apply to the file in the line below
    '''
    input_file = "test.jpeg"
    load_and_go(input_file, greens)
    print (calculate(input_file))
   