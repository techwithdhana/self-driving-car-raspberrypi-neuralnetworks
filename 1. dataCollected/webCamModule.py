import cv2

cap = cv2.VideoCapture(0)

def getImg( display = False):
	success, frame = cap.read()
	frame = cv2.resize(frame, (480, 360))
	if display:
		cv2.imshow("image", frame)
	return frame


if __name__ == "__main__":
	while True:
		frame = getImg(True)
