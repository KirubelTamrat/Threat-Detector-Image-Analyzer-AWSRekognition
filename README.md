# Threat-Detector-Image-Analyzer-AWSRekognition
Threat and Safety Image Detector (AWS Rekognition)

This project analyzes images stored in an S3 bucket and checks whether the image contains any unsafe or potentially threatening content. It uses Amazon Rekognition to look for things like violence, weapons, fire, accidents, and other visuals that could be considered harmful. Everything runs in the cloud through a Python Lambda function.

# What this project does

You upload an image into an S3 bucket.
The Lambda function reads the bucket name and file name from the input.
It sends the image to Rekognition, which analyzes the image in two ways:

Moderation analysis. This checks for unsafe content such as violence, blood, weapons, drugs, or anything explicit.

Object and scene detection. This identifies objects in the image, and the function filters out the ones that might be dangerous, such as guns, knives, fire, smoke, or explosions.

The function then returns a simple result.
If threats were found, it lists them along with confidence levels.
If not, it returns a message saying the image appears safe.

# Why I built this

I wanted to build something practical that shows how AWS services can work together to process images and extract real meaning from them. It also helps demonstrate how serverless applications work, since everything happens through S3, Lambda, and Rekognition without needing to manage any servers.

# How the system works

S3 stores the images.
Lambda contains the Python code that processes the request.
Rekognition performs the actual image analysis.
Lambda combines everything and returns a simple JSON response that tells you whether the image is safe or not.

The basic flow looks like this:

Upload an image to S3.
Trigger the Lambda function by passing the bucket name and image name.
Lambda sends the image to Rekognition for analysis.
Lambda returns the final result, which includes any detected threats.

# Requirements

An AWS account.
An S3 bucket to store the images you want to analyze.
A Lambda function using Python 3.
Amazon Rekognition turned on in the same region.
Permissions for the Lambda function to use both S3 and Rekognition.

