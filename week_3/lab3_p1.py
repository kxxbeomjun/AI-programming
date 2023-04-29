#lab3_p1.py

import math

#getting input from user
storage = int(input("Enter USB size (GB): "))

#change to byte
storage=storage * 1000000000 #1,000,000,000 bytes = 1GB

#bytes needed to store the image
GIF = 800 * 600 * 1 / 5 #8bits % 5:1
JPEG = 800 * 600 * 3 / 25
PNG = 800 * 600 * 3 / 8
TIFF = 800 * 600 * 6

#가능한 사진의 개수를 내림함수를 통해 계산
image_GIF= math.floor(storage/GIF)
image_JPEG = math.floor(storage/JPEG)
image_PNG = math.floor(storage/PNG)
image_TIFF = math.floor(storage/TIFF)

#5자리 우측정렬 기준에 맞춰서 출력
print(format(image_GIF, '>5'), "images in GIF format can be stored")
print(format(image_JPEG, '>5'), "images in JPEG format can be stored")
print(format(image_PNG, '>5'), "images in PNG format can be stored")
print(format(image_TIFF, '>5'), "images in TIFF format can be stored")