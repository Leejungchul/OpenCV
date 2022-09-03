import cv2

no = 0
cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret,img = cap.read()
        if ret:
            cv2.imshow('camera',img)
            key = cv2.waitKey(1) & 0xFF  # 눌린 키 저장
            if key == ord('s'):
                cv2.imwrite(f'nomask/nomask_{no}.jpg',img)
                no = no+1
        


        else:
            print('error')
            
else:
    print('Camera error')

cap.release()
cv2.destroyAllWindows()