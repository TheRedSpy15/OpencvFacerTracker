import cv2


def main():
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    video = cv2.VideoCapture(0)
    framesTotal = 0

    while True:
        framesTotal += 1
        check, frame = video.read()
        faceCount = 0

        if check:
            faces = faceCascade.detectMultiScale(frame, 2, 5)

            for x,y,w,h in faces:
                frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0,0,255), 3)
                faceCount += 1
                frame = cv2.putText(frame, "Faces: " + str(faceCount), (25,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

            cv2.imshow("Face Tracker", frame)
            key = cv2.waitKey(1)

            if key == ord('x'):
                break
        else:
            print("Failed check")
            break

    print("Frames (Total): ", framesTotal)
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Interrupted')
		try:
			import sys
			sys.exit(0)
		except SystemExit:
			import os
			os._exit(0)
