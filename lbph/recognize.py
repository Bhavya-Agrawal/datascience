#!/usr/bin/python3

# import the necessary packages
from lbphimagesearch.localbinarypatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import cv2
  
# capture live images  

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

# pass these arguments while running program
#ap.add_argument("-t", "--training", required=True,help="path to the training images")
ap.add_argument("-t", "--training", required=True, help="path to training images")
#ap.add_argument("-e", "--testing", required=True, help="path to the tesitng images")
ap.add_argument("-e", "--testing", required=True, help="path to testing images")
args = vars(ap.parse_args())

# capture real image for testing
cap = cv2.VideoCapture(0)

while cap.isOpened():
	status,frame = cap.read()

	# writing at least 10 images to training dataset
	#for i in range (0,10):
	cv2.imshow('image.jpg',frame)
	cv2.imwrite('testingimages/image.jpg',frame)

	if cv2.waitKey(0) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()

 
print("in progress") 
# initialize the local binary patterns descriptor along with
# the data and label lists
desc = LocalBinaryPatterns(24, 8)
data = []
labels = []

#now applying lbph algorithm over the images
# loop over the training images
for imagePath in paths.list_images(args["training"]):
	#print(imagePath)
	# load the image, convert it to grayscale, and describe it
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	hist = desc.describe(gray)
 
	# extract the label from the image path, then update the
	# label and data lists -1 for after spliting as per / take last element ie actual pic name
	labels.append(imagePath.split("/")[-1])
	data.append(hist)

#print(data)
# train a Linear SVM on the data
model = LinearSVC(C=100.0, random_state=42)
model.fit(data, labels)

# applying svm over the images
# loop over the testing images
for imagePath in paths.list_images(args["testing"]):
	# load the image, convert it to grayscale, describe it,
	# and classify it
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	hist = desc.describe(gray)
	prediction = model.predict(hist.reshape(1, -1))


	imagename = ''.join(prediction)

	imagename = imagename.split('.')
	# display the image and the prediction
	cv2.putText(image, imagename[0], (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
		1.0, (0, 0, 255), 3)
	cv2.imshow("Image", image)
	cv2.waitKey(0)
	break