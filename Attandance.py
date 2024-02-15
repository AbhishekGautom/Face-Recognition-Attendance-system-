import cv2
import numpy as np
import face_recognition

imgAditiya2222 = face_recognition.load_image_file('Images/Aditiya2222.jpeg')
imgAditiya2222 = cv2.cvtColor(imgAditiya2222, cv2.COLOR_BGR2RGB)

imgAbhishek3333 = face_recognition.load_image_file('Images/Abhishek3333.jpeg')
imgAbhishek3333 = cv2.cvtColor(imgAbhishek3333, cv2.COLOR_BGR2RGB)

imgAniket9999 = face_recognition.load_image_file('Images/Aniket9999.jpeg')
imgAniket9999 = cv2.cvtColor(imgAniket9999, cv2.COLOR_BGR2RGB)

imgFarooq8888 = face_recognition.load_image_file('Images/Farooq8888.jpeg')
imgFarooq8888 = cv2.cvtColor(imgFarooq8888, cv2.COLOR_BGR2RGB)

imgPrerak5555 = face_recognition.load_image_file('Images/Prerak5555.jpeg')
imgPrerak5555 = cv2.cvtColor(imgPrerak5555, cv2.COLOR_BGR2RGB)

facLoc = face_recognition.face_locations(imgAditiya2222)[0]
encodedAditiya2222 = face_recognition.face_encodings(imgAditiya2222)[0]
cv2.rectangle(imgAditiya2222,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

facLoc = face_recognition.face_locations(imgAbhishek3333)[0]
encodedAbhishek3333 = face_recognition.face_encodings(imgAbhishek3333)[0]
cv2.rectangle(imgAbhishek3333,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

facLoc = face_recognition.face_locations(imgAniket9999)[0]
encodedAniket9999 = face_recognition.face_encodings(imgAniket9999)[0]
cv2.rectangle(imgAniket9999,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

facLoc = face_recognition.face_locations(imgFarooq8888)[0]
encodedFarooq8888 = face_recognition.face_encodings(imgFarooq8888)[0]
cv2.rectangle(imgFarooq8888,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

facLoc = face_recognition.face_locations(imgPrerak5555)[0]
encodedPrerak5555 = face_recognition.face_encodings(imgPrerak5555)[0]
cv2.rectangle(imgPrerak5555,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodedAditiya2222],encodedAditiya2222)
results = face_recognition.compare_faces([encodedAbhishek3333],encodedAbhishek3333)
results = face_recognition.compare_faces([encodedAniket9999],encodedAniket9999)
results = face_recognition.compare_faces([encodedFarooq8888],encodedFarooq8888)
results = face_recognition.compare_faces([encodedPrerak5555],encodedPrerak5555)

faceDis = face_recognition.face_distance([encodedAditiya2222],encodedAditiya2222)
faceDis = face_recognition.face_distance([encodedAbhishek3333],encodedAbhishek3333)
faceDis = face_recognition.face_distance([encodedAniket9999],encodedAniket9999)
faceDis = face_recognition.face_distance([encodedFarooq8888],encodedFarooq8888)
faceDis = face_recognition.face_distance([encodedPrerak5555],encodedPrerak5555)

print(results,faceDis)

cv2.putText(imgAditiya2222,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
cv2.putText(imgAbhishek3333,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
cv2.putText(imgAniket9999,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
cv2.putText(imgFarooq8888,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
cv2.putText(imgPrerak5555,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)

cv2.imshow('Aditiya2222', imgAditiya2222)
cv2.imshow('Abhishek3333',imgAbhishek3333)
cv2.imshow('Aniket9999', imgAniket9999)
cv2.imshow('Farooq8888', imgFarooq8888)
cv2.imshow('Prerak5555', imgPrerak5555)


cv2.waitKey(0)
