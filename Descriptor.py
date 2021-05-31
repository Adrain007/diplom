# import numpy
# import cv2
# from matplotlib import pyplot as plt
#
# img = cv2.imread("img/result.png", cv2.IMREAD_GRAYSCALE)
#
# contour = []
# contour, hierarchy = cv2.findContours(
#     img,
#     cv2.RETR_EXTERNAL,
#     cv2.CHAIN_APPROX_NONE,
#     contour)
#
# print(contour)
# contour_array = contour[0][:, 0, :]
# contour_complex = numpy.empty(contour_array.shape[:-1], dtype=complex)
# contour_complex.real = contour_array[:, 0]
# contour_complex.imag = contour_array[:, 1]
# fourier_result = numpy.fft.fft(contour_complex)
# print(fourier_result)
# cv2.imshow("Gaussian Smoothing", numpy.hstack((img, fourier_result)))
# cv2.waitKey(0)  # waits until a key is pressed
# cv2.destroyAllWindows()  # destroys the window showing image
import numpy as np
import cv2

from pyspark.sql.types import *

DecimalType(18, 2)
ShortType
im = cv2.imread("img/test.png")
imgray = cv2.imread("img/test.png", cv2.IMREAD_GRAYSCALE)
# imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(imgray, THRESHOLD, 255, 0)
# ret, thresh = cv2.threshold(imgray, 180, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(imgray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours detected = %d" % len(contours))
CONTOUR = 0
cv2.drawContours(im, contours, CONTOUR, (0, 0, 255), 2)
area = cv2.contourArea(contours[CONTOUR])
print(area)
contour_array = contours[CONTOUR][:, 0, :]
contour_complex = np.empty(contour_array.shape[:-1], dtype=complex)
contour_complex.real = contour_array[:, 0]
contour_complex.imag = contour_array[:, 1]
fourier_result = np.fft.fft(contour_complex)
print(fourier_result[:19])
cv2.imshow("Contours", im)
np.set_printoptions(threshold=np.inf)
coords = np.array2string(contours[CONTOUR])
# open("contour_%d.txt" % CONTOUR, "w").write(coords)
cv2.waitKey(0)
cv2.destroyAllWindows()
