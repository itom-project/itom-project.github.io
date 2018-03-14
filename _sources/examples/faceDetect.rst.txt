=======================================
Face detection
=======================================

With the support of Python 3 and OpenCV 3 lots of image processing can be done with ease.
In this example we show a simple itom script to detect faces off a webcam live image.

Detection with Webcam
-----------------------------------------

First of all, we need to start the camera with the PLUGIN OpenCVGrabber.
The best result for face detection is accomplished with gray images, disregarding the color profile.
Using the OpenCV CascadeClassifier function and the MultiScale Detection it returns coordinates of the ROI of the Feature (--> Face)
With the Coordinate we simply draw a rectangle onto the image ROI.

We also built a small `GUI <..\\_static\\examples\\faceDetect.ui>`_ (Right-click->Save) for seeing a LIVE image of the webcam and a snapshot feature to start calculating the faces.

If you need further assistance, check out the links below.

.. code::

	import cv2
	import numpy as np

	def detect(img, cascade):
		rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4)
		if len(rects) == 0:
			return []
		rects[:,2:] += rects[:,:2]
		return rects

	def draw_rects(img, faces, color):
		for x1, y1, x2, y2 in faces:
			cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)

	def autoGrabbing_changed(checked):
		if(checked):
			cam.enableAutoGrabbing()
		else:
			cam.disableAutoGrabbing()
			
	def snap():
		d = dataObject()
		cam.startDevice()
		autoGrabbingStatus = cam.getAutoGrabbing()
		cam.disableAutoGrabbing()
		cam.acquire()
		cam.getVal(d)
		img=np.array(d)
		faces = detect(img, cascade)
		draw_rects(img, faces, (255, 255, 255))
		win.plot["source"] = img
		if(autoGrabbingStatus):
			cam.enableAutoGrabbing()
		cam.stopDevice()

	def live():
		win.plot["camera"] = cam

	def __del__():
		del cam
		gc()

	if __name__ == '__main__':

		win = ui("FaceDetect.ui", ui.TYPEWINDOW, childOfMainWindow = True)
		cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		nested = cv2.CascadeClassifier('haarcascade_eye.xml')

		try:
			cam= dataIO("OpenCVGrabber",0,'gray')
		except Exception:
			cam = dataIO("DummyGrabber",2048,1024,8)

		#Connect buttons to program
		win.btnSnap.connect("clicked()", snap)
		win.btnLive.connect("clicked()", live)
		win.checkAutoGrabbing.connect("clicked(bool)", autoGrabbing_changed)
		#Initialize gui elements
		win.checkAutoGrabbing["checked"] = cam.getAutoGrabbing()
		#start GUI
		win.show(0)


Result
----------

.. image:: ..\\_static\\examples\\facedetect.jpg
    :alt: Facedetection
    :width: 90%
    :align: center
	
.. raw:: html
	
	<hr>

Resources
-------------------------------

`Face Detection with Python and OpenCV <https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial>`_

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/88HdqNDQsEk?rel=0" frameborder="0" allowfullscreen></iframe>

