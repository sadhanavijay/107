import cv2
video = cv2.VideoCapture("bb3.mp4")
while True:
    check, img = video.read()   
    cv2.imshow("result", img)
    if cv2.waitKey(25)==32:
        break
video.release()
cv2.destroyALLwindows()