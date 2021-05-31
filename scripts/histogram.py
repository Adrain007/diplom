import cv2
import numpy

img = cv2.imread('../img/sem.png')
img_to_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_to_yuv[:, :, 0] = cv2.equalizeHist(img_to_yuv[:, :, 0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)

cv2.imwrite('../img/histogram.png', hist_equalization_result)
src = cv2.imread('../img/histogram.png', cv2.IMREAD_UNCHANGED)

# apply guassian blur on src image
dst = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)

# display input and output image
# cv2.imshow("Gaussian Smoothing", numpy.hstack((src, dst)))
# cv2.waitKey(0)  # waits until a key is pressed
# cv2.destroyAllWindows()  # destroys the window showing image
cv2.imwrite('../img/gaussian.png', dst)

source = cv2.imread("../img/gaussian.png")
final = cv2.medianBlur(source, 3)
cv2.imwrite('../img/median.png', final)

img = cv2.imread("../img/median.png")

ret, threshold = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)

cv2.imwrite('../img/result.png', threshold)


