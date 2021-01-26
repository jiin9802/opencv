#1초마다 5개의 사진을 슬라이드쇼로 보여주는 형식. 아무 버튼이나 눌리면 슬라이드쇼는 끝난다. 

import cv2
import sys
import glob

img_files=glob.glob('.\\images\\*.jpg')

if not img_files:
    print("There are no jpg files in 'images' folder")
    sys.exit()

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx=0

while True:
    img=cv2.imread(img_files[idx])
    if img is None:
        print("Image load failed!")
        break

    cv2.imshow('image',img)
    if cv2.waitKey(1000)>=0: #1초마다 바뀌는데 아무 키나 눌리면 끝남break
        break

    idx+=1
    if idx>=cnt:
        idx=0

cv2.destroyAllWindows()
