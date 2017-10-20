import cv2
import numpy as np

#video capture vs image capture
#better results for real time feedback versus individual images which may be more effective per
#individual frames but not necessarily accurate for long term duration
cap = cv2.VideoCapture(0)
#red hat
while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#hsv hue sat value
	lower_red = np.array([150,150,50])
	upper_red = np.array([180,255,150])

	#lower_gray = np.array([10,20,75])
        #upper_gray = np.array([30,60,99])
	
	mask = cv2.inRange(hsv, lower_red, upper_red) # 1 means in range, refers to the result of the inRange command
	result = cv2.bitwise_and(frame, frame, mask = mask)

        kernel = np.ones((15,15), np.float32)/225
        smoothed = cv2.filter2D(result, -1, kernel)

        #various blurs to help clear out background noise
        blur = cv2.GaussianBlur(result, (15,15), 0)
        median = cv2.medianBlur(result, 15)
        bilateral = cv2.bilateralFilter(result, 15, 75, 75)
        #mess with bilateral filter to see if it can give better results and read into specifically what this
        #function's documentation can provide some insight, read more into HSV filtering applications. 
        
	#displaying the results, with the base feed designated frame as the control
        #commented out display instructions show the intermediate results before getting
        #to the ones that demonstrate the blurs. 

	cv2.imshow('frame', frame)
	#cv2.imshow('mask', mask)
	cv2.imshow('result', result)
	#cv2.imshow('smoothed', smoothed)
        cv2.imshow('blur', blur)
        cv2.imshow('median', median)
        cv2.imshow('bilateral', bilateral)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2.destroyAllWindows()
cap.release()

