import cv2
import os
from glob import glob

image_folder = './animation'
video_name = 'pcd_registration.avi'

images = glob(image_folder+"/*.jpg")
images.sort()

frame = cv2.imread(images[0])
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width, height))

for index in range(len(images)):
    img_path = f'./animation/frame_{index}.jpg' 
    video.write(cv2.imread(img_path))

cv2.destroyAllWindows()
video.release()
