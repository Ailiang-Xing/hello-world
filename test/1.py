import cv2

img = cv2.imread(r"C:\Users\Eric\Desktop\new.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(r"D:\PyCharm 2020.2.1\pythonProject4\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow('Image', resized)
cv2.waitKey(0)

111D:\PyCharm 2020.2.1\pythonProject4\1.py