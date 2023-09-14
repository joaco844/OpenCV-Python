import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('2.jpg')
imgAux = img.copy()
while True:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    count = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cara = imgAux[y:y+h,x:x+w]
        cara = cv2.resize(cara, (150, 150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('cara_{}.jpg'.format(count), cara)
        count = count + 1
    cv2.imshow('img', img)
    cv2.imshow('cara', cara)
    cv2.waitKey(0)
img.release()
