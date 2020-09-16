import cv2
import numpy as np
draw_board = np.ones([720,1280,3],'uint8')*255
drawing = False
color = (0,0,0) #by default black color sketch
radius = 5

def callback(event, x, y, flags, param):
	global draw_board, drawing
	if event == cv2.EVENT_LBUTTONDOWN: #when mouse button is pressed
		drawing = True
		cv2.circle(draw_board,(x,y),radius,color,-1)
	elif event == cv2.EVENT_MOUSEMOVE and drawing == True: #keep drawing circles to simulate writing
		cv2.circle(draw_board,(x,y),radius,color,-1)
	elif event == cv2.EVENT_LBUTTONUP: #when mouse pressed button is left up then stop
		drawing = False

cv2.namedWindow("draw_board")
cv2.setMouseCallback("draw_board", callback)
while True:
	cv2.imshow("draw_board",draw_board)
	key = cv2.waitKey(1) & 0xFF
	# For color of sketch
	if key == ord('b'):
		radius = 5
		color = (255,0,0)
		
	elif key == ord('r'):
		radius = 5
		color = (0,0,255)

	elif key == ord('g'):
		radius = 5
		color = (0,255,0)

	# Eraser
	elif key == ord('e') :
		radius = 15
		color = (255,255,255)
	
	elif key == ord('q'):
		break

cv2.destroyAllWindows()