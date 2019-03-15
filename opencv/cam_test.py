import cv2

cap = cv2.VideoCapture()
template = cv2.imread('image/test_target.jpg', 0)

while True:
    ret1, img_0 = cap.read()
    #img_1 = cv2.cvtColor(img_0, cv2.COLOR_BGR2GRAY)
    cv2.imshow('result', img_0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
