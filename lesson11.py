import cv2
from PIL import Image
image_path = 'cat.jpg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_path)
glasses = Image.open('glass.png')
cat = cat.convert('RGBA')
glasses = glasses.convert('RGBA')

for(x,y,w,h) in cat_face:
    glasses = glasses.resize((w, int(h/2)))
    cat.paste(glasses, (x,int(y+h/4)), glasses)
    cat.save('cat_with_glasses.png')
    cat_w_g = cv2.imread('cat_with_glasses.png')
    cv2.imshow('cat_with_glasses', cat_w_g)
    cv2.waitKey()
#cv2.imshow('cat', image)
#cv2.waitKey()