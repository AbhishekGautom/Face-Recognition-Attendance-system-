'''import cv2
import numpy as np
import face_recognition
import os

path = 'Images'
images = []

classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}.jpg')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])

print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markattandance(names):
    with open('attandance.csv','r+') as f:
        myList = f.readline()
        namelist = []
        for line in myList:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

markattandance('Abhishek3333')

markattandance('a')

encodeListKnow = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0),None,0.25,0.255)
    imgS = cv2.cvtColor(img, (0, 0), None, 0.25, 0.255)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition,face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnow,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)


        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = facesLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markattandance('name')



    cv2.imshow('Webcam','img')
    cv2.waitKey(1)'''







# facLoc = face_recognition.face_locations(imgAditiya2222)[0]
# encodedAditiya2222 = face_recognition.face_encodings(imgAditiya2222)[0]
# cv2.rectangle(imgAditiya2222,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

# facLoc = face_recognition.face_locations(imgAbhishek3333)[0]
# encodedAbhishek3333 = face_recognition.face_encodings(imgAbhishek3333)[0]
# cv2.rectangle(imgAbhishek3333,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

# facLoc = face_recognition.face_locations(imgAniket9999)[0]
# encodedAniket9999 = face_recognition.face_encodings(imgAniket9999)[0]
# cv2.rectangle(imgAniket9999,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

# facLoc = face_recognition.face_locations(imgFarooq8888)[0]
# encodedFarooq8888 = face_recognition.face_encodings(imgFarooq8888)[0]
# cv2.rectangle(imgFarooq8888,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

# facLoc = face_recognition.face_locations(imgPrerak5555)[0]
# encodedPrerak5555 = face_recognition.face_encodings(imgPrerak5555)[0]
# cv2.rectangle(imgPrerak5555,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
# from PIL import ImageGrab
 
path = 'Images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
 
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
 
def markAttendance(name):
    with open('Attandance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
 
#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr
 
encodeListKnown = findEncodings(images)
print('Encoding Complete')
 
cap = cv2.VideoCapture(0)
 
while True:
    success, img = cap.read()
    #img = captureScreen()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
 
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)
 
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
 
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)