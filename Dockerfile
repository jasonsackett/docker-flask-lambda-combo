# syntax=docker/dockerfile:1

### uncomment this line for lambda deploy (and comment out flask section below)
FROM public.ecr.aws/lambda/python:3.8 as requirements
COPY requirements.txt /tmp
RUN pip install --no-cache-dir --target ${LAMBDA_TASK_ROOT} -r /tmp/requirements.txt
FROM public.ecr.aws/lambda/python:3.8 as handler
COPY --from=requirements $LAMBDA_TASK_ROOT $LAMBDA_TASK_ROOT
COPY app.py ${LAMBDA_TASK_ROOT}
CMD [ "app.handler" ]

# to deploy:
#   as usual,
#       1) log into aws,
#       2) docker build,
#       3) tag,
#       4) push to ECR,
#       5) redeploy lambda function from ECR image

### uncomment this section to run as flask (and comment out lambda section above)
#FROM python:3.8-slim-buster
#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt
#COPY . .
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# docker build:
#   docker build --tag flask2 --network=host .
# docker run:
#   docker run --network=host -d -p 5000:5000 flask2
# test example:
#   http://localhost:5000/hellox/7
