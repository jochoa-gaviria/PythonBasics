import cv2
path='./Files/photos/'
faceCascade=cv2.CascadeClassifier(path+'haarcascade_frontalface_default.xml')
img=cv2.imread(path+'photo1.jpg', 1)
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert img into a gray scale

faces=faceCascade.detectMultiScale(gray_img, 
scaleFactor=1.05,
minNeighbors=50)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y),(x+w, y+h), (0,0,255), 3)

print(type(faces))
print(faces)

resized=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()