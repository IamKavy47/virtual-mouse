import cv2
import numpy as np
import HandTrackingModul as htm
import time
import autopy  # Import autopy for mouse control

##########################
wCam, hCam = 640, 480  # Camera resolution
frameR = 100  # Frame Reduction for movement frame
smoothening = 7  # Smooth movement
##########################

pTime = 0
plocX, plocY = 0, 0  # Previous location
clocX, clocY = 0, 0  # Current location

cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # Set width
cap.set(4, hCam)  # Set height
detector = htm.handDetector(max_hands=1)  # Using updated module
wScr, hScr = autopy.screen.size()  # Get screen size
# print(wScr, hScr)

while True:
    # 1. Find hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Index finger tip
        x2, y2 = lmList[12][1:]  # Middle finger tip

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        # Draw frame rectangle for movement
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        # 4. Moving Mode: Only Index Finger
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert coordinates to screen size
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            # 6. Smoothen values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # 7. Move mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

            plocX, plocY = clocX, clocY  # Update previous location

        # 8. Clicking Mode: Both Index and Middle Fingers Up
        if fingers[1] == 1 and fingers[2] == 1:
            # Find distance between index and middle fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)

            # Click mouse if distance is short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

    # 9. Frame rate display
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

    # 10. Display image
    cv2.imshow("Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
