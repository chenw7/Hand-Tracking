#This program utilizes a class structure and utilizes the mediapipe and opencv library to track the user's hand motions and identify as left or right hand.
#Author @Wei-cen Chen
#Version January 2, 2022

#Importing the necessary libraries (cv2, mediapipe, and math) to run the program
import cv2
import mediapipe as mp
import math

#Writes the program using a class structure
class HandDetector:

    def __init__(self, mode=False,maxHands=2, detectionCon=0.5, minTrackCon=0.5):
        
        #initializing variables and lists to be implemented later
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.minTrackCon = minTrackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon, min_tracking_confidence = self.minTrackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []

    def findHands(self, img, draw=True, flipType=True):
       
        #Converts the image into a BGR image.
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        allHands = []
        h, w, c = img.shape
        
        #if a hand is detected, store the landmarks in a list
        if  self.results.multi_hand_landmarks:
            for handType,handLms in zip(self.results.multi_handedness,self.results.multi_hand_landmarks):
                myHand={}
                ## lmList
                mylmList = []
                xList = []
                yList = []
                for id, lm in enumerate(handLms.landmark):
                    px, py = int(lm.x * w), int(lm.y * h)
                    mylmList.append([px, py])
                    xList.append(px)
                    yList.append(py)

                #Determining the dimensions of the box
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                boxW, boxH = xmax - xmin, ymax - ymin
                bbox = xmin, ymin, boxW, boxH
                cx, cy = bbox[0] + (bbox[2] // 2), \
                         bbox[1] + (bbox[3] // 2)

                myHand["lmList"] = mylmList
                myHand["bbox"] = bbox
                myHand["center"] =  (cx, cy)

                #Determine if the hand is left or right hand
                if flipType:
                    if handType.classification[0].label =="Right":
                        myHand["type"] = "Left"
                    else:
                        myHand["type"] = "Right"
                else:
                    myHand["type"] = handType.classification[0].label
                    allHands.append(myHand)

                #Determine and draw a rectangle around the detected hand & Label hand as left or right
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
                    cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                                  (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20),
                                  (255, 0, 255), 2)
                    cv2.putText(img,myHand["type"],(bbox[0] - 30, bbox[1] - 30),cv2.FONT_HERSHEY_PLAIN,
                                2,(255, 0, 255),2)
        if draw:
            return allHands,img
        else:
            return allHands

    def fingersUp(self,myHand):
        #Tracks the fingers that are up in both hands (if they are detected)
        
        myHandType =myHand["type"]
        myLmList = myHand["lmList"]
        if self.results.multi_hand_landmarks:
            fingers = []
            # Thumb
            if myHandType == "Right":
                if myLmList[self.tipIds[0]][0] > myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if myLmList[self.tipIds[0]][0] < myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if myLmList[self.tipIds[id]][1] < myLmList[self.tipIds[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers

    def findDistance(self,p1, p2, img=None):

        #Variables to determine where to draw the circles on the fingers
        x1, y1 = p1
        x2, y2 = p2
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        length = math.hypot(x2 - x1, y2 - y1)
        info = (x1, y1, x2, y2, cx, cy)
        
        #When there are two index fingers detected, find the distance between them and draw a line connecting the two
        if img is not None:
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            return length,info, img
        else:
            return length, info

#This is the part of the program that utilizes all the variables and methods previously declared
def main():
    #enables computer to use web cam
    cap = cv2.VideoCapture(0)
    
    #Declares confidence level as 0.8 (adjust as you need) and maximum number of hands to be 2
    detector = HandDetector(detectionCon=0.8, maxHands=2)
    while True:
        # Get image frame
        success, img = cap.read()
        #Find the hand and its landmarks (the features of the hand that the cv2 library tracks)
        hands, img = detector.findHands(img)  

        #If hands are detected, declare variables and add to declared lists
        if hands:
            #Hand 1
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  #List of 21 Landmark points
            bbox1 = hand1["bbox"]  #Bounding box info x,y,w,h
            centerPoint1 = hand1['center']  #Determines the center of the hand
            handType1 = hand1["type"]  #Determines if the hand is left or right hand 

            fingers1 = detector.fingersUp(hand1)

            #If the length of the list is 2, then there are two hands. Perform same actions that were performed on first hand.
            if len(hands) == 2:
                #Hand 2
                hand2 = hands[1]
                lmList2 = hand2["lmList"]  # List of 21 Landmark points
                bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
                centerPoint2 = hand2['center']  # center of the hand cx,cy
                handType2 = hand2["type"]  # Hand Type "Left" or "Right"

                fingers2 = detector.fingersUp(hand2)

                # Find Distance between two Landmarks. Could be same hand or different hands
                length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
                # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
        
        # Display everything
        cv2.imshow("Image", img)
        cv2.waitKey(1)

#Execute the program
if __name__ == "__main__":
    main()
