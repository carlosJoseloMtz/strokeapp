__author__ = 'carlosdev'


import cv

'''
    Class: Gets camera access by opencv.
    Author: Carlos Mtz
    Team: NopalDev
'''


class CameraAccess:

    def __init__(self, camera_index, auto_init = True):
        """
        Inits the object with a camera target,
        camera it's access by default, you can set it up as
        false, so you can manually access later.
        :param camera_index: index of the camera on your system that you're trying to access.
        :param auto_init: indicates if it gets the capture from constructor,
        or waits to do it manually, it's auto access by default.
        """
        self.camera_index = camera_index
        if auto_init:
            self.capture = cv.CaptureFromCAM(self.camera_index)
        else:
            self.capture = None
        print 'camera init'
        self.frame = None

    def init_camera(self):
        """
        Starts the camera, in case you set it up as False in constructor.
        """
        if self.capture is None:
            self.capture = cv.CaptureFromCAM(self.camera_index)

    def get_image(self):
        """
        Gets the frame image so it can be displayed or process as you wish.
        :rtype : QueryFrame type.
        :return: returns the frame gotten on cam.
        """
        self.frame = cv.QueryFrame(self.capture)
        return self.frame

