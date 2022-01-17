import cv2
def takeSnapshot():
    vco=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vco.read()
        cv2.imwrite("picture1.jpg",frame)
        result=False
    vco.release()
    cv2.destroyAllWindows()
takeSnapshot()
