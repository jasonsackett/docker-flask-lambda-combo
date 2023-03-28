This is a simple template for a python app that is Dockerized for
either/both use as a 
flask web app
and/or an
AWS docker lambda function

see notes in app.py, and Dockerfile for instructions

Steps to push lambda docker to ECR:

Retrieve an authentication token and authenticate your Docker client to your registry.
Use the AWS CLI:

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin XXXXX.dkr.ecr.us-east-1.amazonaws.com

Note: If you receive an error using the AWS CLI, make sure that you have the latest version of the AWS CLI and Docker installed.
Build your Docker image using the following command. For information on building a Docker file from scratch see the instructions here 
. You can skip this step if your image is already built:

docker build -t docker-flask-lambda-combo .

After the build completes, tag your image so you can push the image to this repository:

docker tag docker-flask-lambda-combo:latest XXXXX.dkr.ecr.us-east-1.amazonaws.com/docker-flask-lambda-combo:latest

Run the following command to push this image to your newly created AWS repository:

docker push XXXXX.dkr.ecr.us-east-1.amazonaws.com/docker-flask-lambda-combo:latest
