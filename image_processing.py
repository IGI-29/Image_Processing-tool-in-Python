import PIL
import pytesseract as tess
from PIL import Image

tess.pytesseract.tesseract_cmd = r'C:\Users\ACER\AppData\Local\Tesseract-OCR\tesseract.exe'

img_path = input("Enter the Path of Image to Process : ")

# adding image path
img = Image.open(img_path)
print('Welcome to Image Processing, Choose your Command from Below')

# receiving commands from user
print("Press 1 for resize the image")
print("Press 2 for cropping the image")
print("Press 3 for rotating the image")
print("Press 4 for flipping the image")
print("Press 5 for making the image Greyscale (B&W)")
print("Press 6 for Compressing the Image")
print("Press 7 for Converting Image Format")
print("Press 8 for Converting Image to text")
n = int(input())
# print(img.size)

if (n == 1):
    a = int(input("Enter Dimension 1 : "))
    b = int(input("Enter Dimension 2 : "))
    img_small = img.resize((a, b))
    m = int(input("Press 1 to also Save the Image on Desktop : "))
    if (m == 1):
        img_small.save('C:/Users/ACER/Desktop/resized.jpg')
        print("Image will be Saved at Desktop, Press Enter to Exit")
        j = input()
    img_small.show()

if (n == 2):
    a, b = [int(x) for x in input("Enter the Top-Left Valid Coordinates : ").split()]
    c, d = [int(x) for x in input("Enter the Bottom-Right Valid Coordinates : ").split()]
    cropped_img = img.crop((a, b, c, d))
    m = int(input("Press 1 to also Save the Image on Desktop : "))
    if (m == 1):
        cropped_img.save('C:/Users/ACER/Desktop/cropped.jpg')
        print("Image will be Saved at Desktop, Press Enter to Exit")
        j = input()
    cropped_img.show()

if (n == 3):
    a = int(input("Enter the Degree Angle to Rotate the Image Anti-clockwise: "))
    rotate_img = img.rotate(a)
    # m = int(input("Press 1 to also Save the Image on Desktop : "))

    rotate_img.save('C:/Users/ACER/Desktop/rotated.jpg')
    print("Image will be Saved at Desktop, Press Enter to Exit")
    j = input()
    rotate_img.show()

if (n == 4):
    a = int(input("Press 1 to flip Horizontally and 2 to flip Vertically : "))
    if (a == 1):
        flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    if (a == 2):
        flip_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        flip_img = img
    # m = int(input("Press 1 to also Save the Image on Desktop : "))

    flip_img.save('C:/Users/ACER/Desktop/flipped.jpg')
    print("Image will be Saved at Desktop, Press Enter to Exit")

    j = input()
    flip_img.show()

if (n == 5):
    bw_img = img.convert('L')
    m = int(input("Press 1 to also Save the Image on Desktop : "))
    if (m == 1):
        bw_img.save('C:/Users/ACER/Desktop/B&WImage.jpg')
        print("Image will be Saved at Desktop, Press Enter to Exit")
        j = input()
        bw_img.show()

if (n == 6):
    w = img.size[0]
    wp = (w / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wp)))
    compressed_img = img.resize((w, hsize), PIL.Image.ANTIALIAS)
    compressed_img.save('C:/Users/ACER/Desktop/compressed.jpg')
    print("Image will be Saved at Desktop, Press Enter to Exit")
    j = input()

if (n == 7):
    print("Press 1 to Convert to JPG")
    print("Press 2 to Convert to PNG")
    print("Press 3 to Convert to JFIF")
    k = int(input())
    if (k == 1):
        img.save('C:/Users/ACER/Desktop/Converted.jpg')
    if (k == 2):
        img.save('C:/Users/ACER/Desktop/Converted.png')
    if (k == 3):
        img.save('C:/Users/ACER/Desktop/Converted.jfif')
    print("Image will be Saved at Desktop, Press Enter to Exit")
    j = input()

if (n == 8):
    text = tess.image_to_string(img)
    print(text)
    print("Press Enter to Exit")
    j = input()
