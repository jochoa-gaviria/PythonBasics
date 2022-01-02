import cv2, time
path='./Files/videos/'
video=cv2.VideoCapture(0)
a=0
while True:
    a+=1
    check, frame = video.read()

    print(check)
    print(frame)


    # time.sleep(2)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    cv2.imshow('video',gray)
  
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()