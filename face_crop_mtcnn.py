# Importing Required Libraries
from mtcnn import MTCNN
import cv2
import pickle
import os

# Initialise MTCNN detector for face detection
detector = MTCNN() 

# Additional actor name list which are not available in data directory
actors = pickle.load(open('downloaded_actors_images.pkl','rb'))

# Extracting filenames from all the sub-directory present in data directory
filenames = []
for actor in actors:
    for file in os.listdir(os.path.join('data',actor)):
        filenames.append(os.path.join('data',actor,file))

# Detecting only face from the image and write it again with same filename
for file in filenames:
    if os.path.isfile(file):
        try:
            image = cv2.imread(file)
            output = detector.detect_faces(image)

            for i in output:
                x, y, width, height = i['box']
                cropped_img = image[y : y+height, x : x+width]
                
                # cv2.rectangle(image, pt1 =( x, y), pt2 =(x + width, y + height), color=(255,0,0), thickness=3)
                # cv2.imshow('Face Detection',cropped_img)
                # cv2.waitKey(0)
                
                cv2.imwrite(file, cropped_img)
        except:
            print('Something went wrong! when writing to the file')
            
    else:
        print('File Not Saved')



