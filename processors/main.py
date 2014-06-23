__author__ = 'carlosdev'

from ColorFinder import ColorFinder
import threading
from CameraAccess import CameraAccess
import cv


global five_seconds_passed
five_seconds_passed = False

def say_it_passed():
    global five_seconds_passed
    five_seconds_passed = True
    #print 'object detected during five seconds!'

def repeat():
    global five_seconds_passed
    cv.NamedWindow("w", cv.CV_WINDOW_AUTOSIZE)
    camera = CameraAccess(0)

    green_color_finder = ColorFinder((20, 100, 100), (60, 255, 255))
    #blue_color_finder = ColorFinder((110,50,50), (130,255,255))
    #TODO: find blue color so you can test the speed detection of several patterns at the same time
    found_color = False
    is_counting = False
    missed_frames_counter = 0
    recognized_counter = 0
    while True:
        img = camera.get_image()
        green_point_found = green_color_finder.find_color(img)

        #blue_point_found = blue_color_finder.find_color(img)
        #if blue_point_found is not None:
        #    cv.Circle(img, blue_point_found, 2, (255, 255, 255), 20)


        found_color = False
        if green_point_found is not None: #if object with based color was found, draw a little circle just right in the center
            cv.Circle(img, green_point_found, 2, (255, 255, 255), 20)
            found_color = True
        cv.ShowImage("w", img)

        if not found_color and is_counting:
            missed_frames_counter += 1
            found_color = True

        if missed_frames_counter > 22:
            missed_frames_counter = 0
            print 'object missed'
            found_color = False

        if five_seconds_passed:
            recognized_counter += 1
            print 'object detected for five seconds', recognized_counter

        if five_seconds_passed or (is_counting and not found_color):
            five_seconds_passed = False
            missed_frames_counter = 0
            found_color = False
            is_counting = False
            timer.cancel()

        if found_color and not is_counting:
            timer = threading.Timer(5.0, say_it_passed)
            is_counting = True
            timer.start()
            print 'object detected on frame'
        key = cv.WaitKey(10)
        if key == 1048603:
            break
    cv.DestroyWindow("w")

repeat()