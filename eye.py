"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"
    elif gaze.is_top():
        text = "Looking up"
    elif gaze.is_bottom():
        text = "Looking down"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()


# Model file - gaze_tracking.py

class Eye:
    def middle_point(self, p1, p2):
        # Returns the middle point (x, y) between two points
        pass

    def isolate(self, frame, landmarks, points):
        # Isolate an eye, to have a frame without other parts of the face
        pass

    def blinking_ratio(self, landmarks, points):
        # Calculates a ratio that can indicate whether an eye is closed or not.
        # It's the division of the width of the eye by its height
        pass

    def analyze(self, original_frame, landmarks, side, calibration):
        # Detects and isolates the eye in a new frame, sends data to the calibration,
        # and initializes Pupil object
        pass


class Calibration:
    def is_complete(self):
        # Returns true if the calibration is completed
        pass

    def threshold(self, side):
        # Returns the threshold value for the given eye
        pass

    def iris_size(self, frame):
        # Returns the percentage of space that the iris takes up on the surface of the eye
        pass

    def find_best_threshold(self, eye_frame):
        # Calculates the optimal threshold to binarize the frame for the given eye
        pass

    def evaluate(self, eye_frame, side):
        # Improves calibration by taking into consideration the given image
        pass


class Pupil:
    def image_processing(self, eye_frame, threshold):
        # Performs operations on the eye frame to isolate the iris
        pass

    def detect_iris(self, eye_frame):
        # Detects the iris and estimates the position of the iris by calculating the centroid
        pass


class GazeTracking:
    def pupils_located(self):
        # Check that the pupils have been located
        pass

    def analyze(self):
        # Detects the face and initializes Eye objects
        pass

    def refresh(self, frame):
        # Refreshes the frame and analyzes it
        pass

    def pupil_left_coords(self):
        # Returns the coordinates of the left pupil
        pass

    def pupil_right_coords(self):
        # Returns the coordinates of the right pupil
        pass

    def horizontal_ratio(self):
        # Returns a number between 0.0 and 1.0 that indicates the horizontal direction of the gaze
        pass

    def vertical_ratio(self):
        # Returns a number between 0.0 and 1.0 that indicates the vertical direction of the gaze
        pass

    def annotated_frame(self):
        # Returns the main frame with pupils highlighted
        pass

    def top(self):
        # Returns true if the user is looking to the top
        pass

    def is_bottom(self):
        # Returns true if the user is looking to the bottom
        pass

    def is_right(self):
        # Returns true if the user is looking to the right
        pass

    def is_left(self):
        # Returns true if the user is looking to the left
        pass

    def is_center(self):
        # Returns true if the user is looking to the center
        pass

    def is_blinking(self):
        # Returns true if the user closes his eyes
        pass
