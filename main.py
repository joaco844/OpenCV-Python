import cv2
from deepface import DeepFace
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('T.jpg')
imgAux = img.copy()
while True:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    count = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cara = imgAux[y:y+h,x:x+w]
        cara = cv2.resize(cara, (150, 150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('cara_{}.jpg'.format(count), cara)
        info = DeepFace.analyze(rgb, actions=['age', 'gender', 'emotion'], enforce_detection= False)
        edad = info[count]
        emociones = info[count]
        gen = info[count]
        print(str(gen) + " de " + str(edad) + " años de edad, con estado de animo " + str(emociones))
        if gen == 'Man':
                gen = 'Hombre'
                if emociones == 'angry':
                    emociones = 'enojado'
                if emociones == 'disgust':
                    emociones = 'disgustado'
                if emociones == 'fear':
                    emociones = 'miedoso'
                if emociones == 'happy':
                    emociones = 'feliz'
                if emociones == 'sad':
                    emociones = 'triste'
                if emociones == 'surprise':
                    emociones = 'sorprendido'
                if emociones == 'neutral':
                    emociones = 'neutral'
        elif gen == 'Woman':
                gen = 'Mujer'
                if emociones == 'angry':
                    emociones = 'enojada'
                if emociones == 'disgust':
                    emociones = 'disgustada'
                if emociones == 'fear':
                    emociones = 'miedosa'
                if emociones == 'happy':
                    emociones = 'feliz'
                if emociones == 'sad':
                    emociones = 'triste'
                if emociones == 'surprise':
                    emociones = 'sorprendida'
                if emociones == 'neutral':
                    emociones = 'neutral'
        cv2.putText(img, str(gen), (65, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(img, str(edad), (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(img, str(emociones), (75, 135), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        count = count + 1
    cv2.imshow('img', img)
    cv2.imshow('cara', cara)
    cv2.waitKey(0)

img.release()

