import cv2

# Загрузка данных
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Считывание картинки
img = cv2.imread(r"data/pic.jpg")

# Конвертация
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Распознование лиц
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Рисуем обводку вокруг лица
for (x, y, w, g) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + g), (255, 0, 0), 2)

# Отображение результата
cv2.imshow('Result', img)
cv2.waitKey()