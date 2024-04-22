FROM public.ecr.aws/lambda/python:3.9
COPY performance.py ${LAMBDA_TASK_ROOT}
#CMD [ "app.lambda_handler" ]
CMD ["performance.lambda_handler"]