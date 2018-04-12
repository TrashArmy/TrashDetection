# This file sets unlabelled bounding boxes on items on items 
# USAGE
# python classify_opencv.py -g trash_dir/frozen_inference_graph.pb -p trash_dir/graph.pbtxt -i test_cup.jpeg
# python classify_opencv.py -g ssd_mobilenet_v1_coco_2017_11_17/frozen_inference_graph.pb -p ssd_mobilenet_v1_coco_2017_11_17/ssd_mobilenet_v1_coco_2017_11_17.pbtxt -i test_people.jpg

# import packages
import numpy as np
import argparse 
import cv2 as cv

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-g", "--inference_graph", required=True,
	help="path to inference graph file")
ap.add_argument("-p", "--graph", required=True,
	help="path to .pbtxt file (protobuf text?)")
ap.add_argument("-i", "--image", required=True, help="image to classify")
ap.add_argument("-o", "--output_image", default="output.jpeg", help="name of output image")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

cvNet = cv.dnn.readNetFromTensorflow(args["inference_graph"], args["graph"])

img = cv.imread(args["image"])
rows = img.shape[0]
cols = img.shape[1]
cvNet.setInput(cv.dnn.blobFromImage(img, 1.0/127.5, (300, 300), (127.5, 127.5, 127.5), swapRB=True, crop=False))
cvOut = cvNet.forward()

for detection in cvOut[0,0,:,:]:
    score = float(detection[2])
    if score > 0.3:
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows
        cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

cv.imwrite(args["output_image"],img)
