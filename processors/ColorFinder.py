__author__ = 'carlosdev'

import cv

'''
    Class: Finds an object based on given color specifications.
    Author: Carlos Mtz
    Team: NopalDev
'''


class ColorFinder:
    def __init__(self, min_color, max_color):
        """
        Inits the object with a min color array and a max color array,
        so it can track it based on this set ups.
        :param min_color: minimum color range
        :param max_color: maximum color range
        """
        self.min_color = min_color
        self.max_color = max_color

    def find_color(self, img):
        """
        Tries to find object with color specifications
        :rtype : (x, y) point, or None
        :param img: image to look for the patters given into the constructor
        :return: None if object wasn't found, an initialized point otherwise.
        """
        cv.Smooth(img, img, cv.CV_BLUR, 3)
        hsv_img = cv.CreateImage(cv.GetSize(img), 8, 3)
        cv.CvtColor(img, hsv_img, cv.CV_BGR2HSV)
        thresholded_img = cv.CreateImage(cv.GetSize(hsv_img), 8, 1)
        cv.InRangeS(hsv_img, self.min_color, self.max_color, thresholded_img)
        image_mat = cv.GetMat(thresholded_img)
        moments = cv.Moments(image_mat)
        area = cv.GetCentralMoment(moments, 0, 0)

        x = 0
        y = 0
        if (area > 100000):
            x = cv.GetSpatialMoment(moments, 1, 0) / area
            y = cv.GetSpatialMoment(moments, 0, 1) / area
            return (int(x), int(y))

        return None